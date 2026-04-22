import requests
import os
import cv2
import logging


def debug_plate(image_path):
    """Check basic image properties"""

    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("❌ OpenCV could not read the image")
        return

    h, w = img.shape[:2]
    print(f"\n📸 Image Info:")
    print(f"   Resolution : {w} x {h} pixels")
    print(f"   File size  : {os.path.getsize(image_path):,} bytes")
    print(f"   Channels   : {img.shape[2] if len(img.shape) > 2 else 1}")
    print(f"   ✅ Image size looks OK")


def test_yolo_only(image_path):
    """Test if YOLO can detect the plate region"""
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    from ultralytics import YOLO

    print(f"\n🔍 Testing YOLO Detection...")

    model_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "best.pt"
    )
    if not os.path.exists(model_path):
        print(f"   ❌ best.pt not found at: {model_path}")
        return False, None

    print(f"   ✅ Model found: {model_path}")

    model       = YOLO(model_path)
    img         = cv2.imread(image_path)
    results     = model(img, conf=0.10, verbose=False)
    crops       = []
    total_boxes = 0

    for result in results:
        for box in result.boxes:
            total_boxes += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf            = float(box.conf[0])

            print(f"   ✅ Plate region detected!")
            print(f"      Box        : ({x1}, {y1}) → ({x2}, {y2})")
            print(f"      Confidence : {conf:.2%}")

            pad  = 15
            crop = img[
                max(0, y1 - pad):min(img.shape[0], y2 + pad),
                max(0, x1 - pad):min(img.shape[1], x2 + pad)
            ]

            crop_path = os.path.join(
                os.path.dirname(image_path), "debug_crop.jpg"
            )
            cv2.imwrite(crop_path, crop)
            print(f"      Crop saved : {crop_path}")
            print(f"      Crop size  : {crop.shape[1]} x {crop.shape[0]} pixels")
            crops.append(crop)

    if total_boxes == 0:
        print("   ⚠️  YOLO found NO plate regions")
        return False, None

    return True, crops


def test_ocr_only(crops):
    """
    Test OCR only on YOLO crops — NOT on full image.
    Full image is too large and causes PaddleOCR to hang.
    """

    # Suppress logs
    logging.getLogger('ppocr').setLevel(logging.ERROR)
    logging.getLogger('paddle').setLevel(logging.ERROR)
    os.environ['GLOG_minloglevel']     = '3'
    os.environ['FLAGS_logtostderr']    = '0'
    os.environ['PADDLE_CPP_LOG_LEVEL'] = '3'
    os.environ['PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK'] = 'True'

    from paddleocr import PaddleOCR

    print(f"\n🔤 Testing OCR on YOLO crops only...")

    reader = PaddleOCR(use_textline_orientation=True, lang='en')

    def run_ocr(img, label):
        """Run OCR and print results"""
        print(f"\n   [{label}]")
        print(f"   Image size: {img.shape[1]} x {img.shape[0]} pixels")

        try:
            result = reader.predict(img)

            if not result:
                print(f"   ⚠️  No text found")
                return

            found_any = False
            for res in result:
                rec_texts  = res.get('rec_text',  [])
                rec_scores = res.get('rec_score', [])
                for text, score in zip(rec_texts, rec_scores):
                    if text.strip():
                        print(f"   → '{text.strip()}' (confidence: {score:.2%})")
                        found_any = True

            if not found_any:
                print(f"   ⚠️  OCR returned empty text")

        except Exception as e:
            print(f"   ❌ OCR Error: {e}")

    if not crops:
        print("   ⚠️  No crops to test OCR on")
        return

    for i, crop in enumerate(crops):
        # Original crop
        run_ocr(crop, f"Crop {i+1} — original")

        # Resized 2.5x
        crop_resized = cv2.resize(
            crop, None, fx=2.5, fy=2.5,
            interpolation=cv2.INTER_CUBIC
        )
        run_ocr(crop_resized, f"Crop {i+1} — 2.5x resized")

        # Top zone only (state name region)
        h, w     = crop_resized.shape[:2]
        top_zone = crop_resized[0:int(h * 0.35), 0:w]
        run_ocr(top_zone, f"Crop {i+1} — top zone (state name)")

        # Bottom zone (plate number region)
        bot_zone = crop_resized[int(h * 0.35):h, 0:w]
        run_ocr(bot_zone, f"Crop {i+1} — bottom zone (plate number)")


def test_plate(image_path):
    """Full pipeline test via Flask backend"""

    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return

    try:
        requests.get('http://localhost:5000/api/test', timeout=10)
    except requests.exceptions.ConnectionError:
        print("❌ Backend is not running.")
        print("   Open a NEW terminal and run: python app.py")
        return
    except requests.exceptions.ReadTimeout:
        print("❌ Backend is not responding.")
        print("   Open a NEW terminal and run: python app.py")
        return

    print("⏳ Sending to full pipeline...")

    try:
        with open(image_path, 'rb') as f:
            response = requests.post(
                'http://localhost:5000/api/process-image',
                files={'images': f},
                timeout=120
            )
    except Exception as e:
        print(f"❌ Error: {e}")
        return

    result = response.json()

    print("\n" + "=" * 40)
    for res in result.get('results', []):
        if res.get('status') == 'processed':
            print(f"Plate Number   : {res['plate_number']}")
            print(f"State of Origin: {res['state_of_origin']}")
            print(f"Confidence     : {res['confidence']}%")
        else:
            print("⚠️  No plate detected in image")
    print("=" * 40 + "\n")


if __name__ == '__main__':
    image_path = r"C:\Users\wurdboss\Desktop\AVLPRDL\test_images\NigCar_12.jpg"

    print("=" * 60)
    print("AVLPRDL - Debug Mode")
    print("=" * 60)

    # Step 1: Check image info
    debug_plate(image_path)

    # Step 2: YOLO detection — get crops
    yolo_ok, crops = test_yolo_only(image_path)

    # Step 3: OCR on crops ONLY (not full image)
    if yolo_ok and crops:
        test_ocr_only(crops)
    else:
        print("\n⚠️  Skipping OCR — no crops from YOLO")

    # Step 4: Full pipeline test
    print(f"\n🚀 Full Pipeline Test...")
    test_plate(image_path)