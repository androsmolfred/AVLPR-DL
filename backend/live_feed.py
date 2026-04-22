# live_feed.py
import threading
import time
import cv2


class LiveFeed:
    """
    Background live camera runner (MJPEG streaming + periodic detection).
    Detection runs in a worker thread so Flask routes never freeze.
    """

    def __init__(
        self,
        detect_fn,
        resize_frame_fn,
        log_callback=None,
        buffer_max=50,
        frame_skip=7,
        detection_cooldown=0.0,
        log_cooldown=30.0,
        stream_jpeg_quality=70,
    ):
        """
        detect_fn(frame, label, do_logging=False) -> (result_dict, evidence_crop_or_none)
        resize_frame_fn(frame) -> resized_frame
        log_callback(result_dict, evidence_crop, label) -> None
        """
        self.detect_fn = detect_fn
        self.resize_frame_fn = resize_frame_fn
        self.log_callback = log_callback

        self.buffer_max = buffer_max
        self.frame_skip = frame_skip
        self.detection_cooldown = detection_cooldown
        self.log_cooldown = log_cooldown

        self.stream_jpeg_quality = stream_jpeg_quality

        self.running = False
        self.cap = None
        self.thread = None

        self.lock = threading.Lock()
        self.latest_frame = None
        self.latest_result = None

        self.buffer = []
        self._detecting = False
        self._last_detection_time = 0.0
        self._last_logged_time = 0.0
        self._last_logged_plate = None

    def start(self, camera_index=0, width=640, height=480, fps=15):
        if self.running:
            return {"status": "already_running"}

        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            return {"status": "error", "message": f"Could not open camera {camera_index}"}

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_FPS, fps)

        with self.lock:
            self.cap = cap
            self.running = True
            self.latest_frame = None
            self.latest_result = None
            self.buffer = []
            self._detecting = False
            self._last_detection_time = 0.0
            self._last_logged_time = 0.0
            self._last_logged_plate = None

        self.thread = threading.Thread(target=self._worker, daemon=True)
        self.thread.start()
        return {"status": "success", "message": "Camera started successfully"}

    def stop(self):
        with self.lock:
            self.running = False
            cap = self.cap
            self.cap = None

        if cap is not None:
            try:
                cap.release()
            except Exception:
                pass

        return {"status": "success", "message": "Camera stopped successfully"}

    def get_latest(self):
        with self.lock:
            return {
                "status": "success",
                "camera_on": self.running,
                "latest": self.latest_result,
            }

    def get_buffer(self):
        with self.lock:
            return list(self.buffer)

    def _push_buffer(self, result_dict):
        with self.lock:
            self.buffer.insert(0, result_dict)
            while len(self.buffer) > self.buffer_max:
                self.buffer.pop()

    def _should_log(self, result_dict):
        if self.log_callback is None:
            return False

        now = time.time()
        plate = (result_dict or {}).get("plate_number")

        if now - self._last_logged_time < self.log_cooldown:
            return False

        # Avoid logging same plate repeatedly (unless cooldown passed)
        if plate and plate == self._last_logged_plate and (now - self._last_logged_time) < (self.log_cooldown + 1):
            return False

        return True

    def _worker(self):
        frame_count = 0

        while True:
            with self.lock:
                if not self.running or self.cap is None:
                    break
                cap = self.cap

            ret, frame = cap.read()
            if not ret:
                time.sleep(0.02)
                continue

            frame_count += 1
            resized = self.resize_frame_fn(frame)

            with self.lock:
                self.latest_frame = resized

            # Only attempt detection every Nth frame
            if frame_count % self.frame_skip != 0:
                time.sleep(0.005)
                continue

            # Cooldown between detections
            now = time.time()
            if self.detection_cooldown > 0 and (now - self._last_detection_time) < self.detection_cooldown:
                time.sleep(0.005)
                continue

            if self._detecting:
                time.sleep(0.005)
                continue

            self._detecting = True
            self._last_detection_time = now

            label = f"live_frame_{frame_count}_{int(now)}"
            try:
                result_dict, evidence_crop = self.detect_fn(resized, label, do_logging=False)

                if result_dict and result_dict.get("status") == "processed":
                    with self.lock:
                        self.latest_result = result_dict

                    # Push to live buffer (frontend can show it immediately)
                    payload = {
                        "plate_number": result_dict.get("plate_number"),
                        "state_of_origin": result_dict.get("state_of_origin"),
                        "confidence": result_dict.get("confidence"),
                        "filename": label,
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    self._push_buffer(payload)

                    # Throttled evidence + Excel logging
                    if self._should_log(result_dict):
                        self._last_logged_time = time.time()
                        self._last_logged_plate = result_dict.get("plate_number")

                        if self.log_callback:
                            self.log_callback(result_dict, evidence_crop, label)

            except Exception:
                # Never crash the camera thread
                pass
            finally:
                self._detecting = False

            time.sleep(0.005)

    def stream_generator(self):
        """
        MJPEG stream generator for Flask endpoint.
        """
        while True:
            with self.lock:
                if not self.running:
                    break
                frame = None if self.latest_frame is None else self.latest_frame.copy()
                result = self.latest_result

            if frame is None:
                time.sleep(0.05)
                continue

            # Overlay latest detection
            if result and result.get("status") == "processed":
                text = f"{result.get('plate_number')} | {result.get('state_of_origin')} | {result.get('confidence')}%"
                cv2.putText(
                    frame,
                    text,
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA
                )

            ok, buf = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, self.stream_jpeg_quality])
            if not ok:
                time.sleep(0.03)
                continue

            jpg_bytes = buf.tobytes()
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" +
                   jpg_bytes +
                   b"\r\n")
            time.sleep(0.03)