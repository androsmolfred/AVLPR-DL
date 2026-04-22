# statelga.py
# Nigeria States and LGA Plate Prefix Lookup
# Plate format: XXX-000-XX  (first 3 letters = LGA code)
# ─────────────────────────────────────────────────────────

# Full state name mapping from common plate/text keywords
NIGERIA_STATES = {
    "ABJ":       "Abuja (FCT)",
    "FCT":       "Abuja (FCT)",
    "ABUJA":     "Abuja (FCT)",
    "ABIA":      "Abia",
    "ADAMAWA":   "Adamawa",
    "AKWA":      "Akwa Ibom",
    "IBOM":      "Akwa Ibom",
    "ANAMBRA":   "Anambra",
    "BAUCHI":    "Bauchi",
    "BAYELSA":   "Bayelsa",
    "BENUE":     "Benue",
    "BORNO":     "Borno",
    "CROSS":     "Cross River",
    "RIVER":     "Cross River",
    "DELTA":     "Delta",
    "EBONYI":    "Ebonyi",
    "EDO":       "Edo",
    "EKITI":     "Ekiti",
    "ENUGU":     "Enugu",
    "GOMBE":     "Gombe",
    "IMO":       "Imo",
    "JIGAWA":    "Jigawa",
    "KADUNA":    "Kaduna",
    "KANO":      "Kano",
    "KATSINA":   "Katsina",
    "KEBBI":     "Kebbi",
    "KOGI":      "Kogi",
    "KWARA":     "Kwara",
    "LAGOS":     "Lagos",
    "CENTRE":    "Lagos",
    "EXCELLENCE":"Lagos",
    "NASARAWA":  "Nasarawa",
    "NIGER":     "Niger",
    "OGUN":      "Ogun",
    "ONDO":      "Ondo",
    "OSUN":      "Osun",
    "OYO":       "Oyo",
    "PLATEAU":   "Plateau",
    "RIVERS":    "Rivers",
    "SOKOTO":    "Sokoto",
    "TARABA":    "Taraba",
    "YOBE":      "Yobe",
    "ZAMFARA":   "Zamfara",
}


# LGA plate prefix codes → State
# First 3 letters of the plate number identify the LGA
# Format: XXX-000-XX
LGA_MAP = {

    # ── Abia ──────────────────────────────────────────────
    "ABA": "Abia",   # Aba North / Aba South
    "BND": "Abia",   # Bende
    "ACH": "Abia",   # Arochukwu
    "HAF": "Abia",   # Isuikwuato / Umunneochi
    "UMA": "Abia",   # Umuahia North / Umuahia South
    "KPU": "Abia",   # Ukwa East / Ukwa West
    "OBG": "Abia",   # Obingwa
    "ISK": "Abia",   # Isiala Ngwa North / Isiala Ngwa South

    # ── Adamawa ───────────────────────────────────────────
    "DSA": "Adamawa",  # Demsa
    "FUR": "Adamawa",  # Fufure
    "GAN": "Adamawa",  # Ganye
    "GRE": "Adamawa",  # Girei
    "GMB": "Adamawa",  # Gombi
    "GUY": "Adamawa",  # Guyuk
    "HNG": "Adamawa",  # Hong
    "JMT": "Adamawa",  # Jada
    "MUB": "Adamawa",  # Mubi North / Mubi South
    "NUM": "Adamawa",  # Numan
    "YLA": "Adamawa",  # Yola North / Yola South
    "MYO": "Adamawa",  # Mayo-Belwa
    "SHE": "Adamawa",  # Shelleng
    "TRG": "Adamawa",  # Toungo

    # ── Akwa Ibom ─────────────────────────────────────────
    "ABK": "Akwa Ibom",  # Abak
    "KRT": "Akwa Ibom",  # Ikot Ekpene
    "KET": "Akwa Ibom",  # Eket
    "KST": "Akwa Ibom",  # Ikot Abasi
    "AFH": "Akwa Ibom",  # Oron
    "AEE": "Akwa Ibom",  # Etinan
    "ETN": "Akwa Ibom",  # Esit Eket
    "UYO": "Akwa Ibom",  # Uyo
    "OKP": "Akwa Ibom",  # Okobo
    "IKN": "Akwa Ibom",  # Ini
    "MKT": "Akwa Ibom",  # Mkpat Enin
    "NSD": "Akwa Ibom",  # Nsit Ibom / Nsit Atai / Nsit Ubium
    "UDG": "Akwa Ibom",  # Udung Uko
    "URU": "Akwa Ibom",  # Uruoffong / Oruk Anam

    # ── Anambra ───────────────────────────────────────────
    "AGU": "Anambra",  # Aguata
    "ABN": "Anambra",  # Anambra East / Anambra West
    "ACA": "Anambra",  # Awka North / Awka South
    "AJL": "Anambra",  # Ayamelum
    "HAL": "Anambra",  # Dunukofia
    "HTE": "Anambra",  # Ekwusigo
    "AWK": "Anambra",  # Idemili North / Idemili South
    "NNE": "Anambra",  # Nnewi North / Nnewi South
    "ONN": "Anambra",  # Onitsha North / Onitsha South
    "OGA": "Anambra",  # Ogbaru
    "OGZ": "Anambra",  # Oyi

    # ── Bauchi ────────────────────────────────────────────
    "BAU": "Bauchi",  # Bauchi
    "BLR": "Bauchi",  # Alkaleri
    "DAS": "Bauchi",  # Dass
    "DKU": "Bauchi",  # Darazo
    "DRZ": "Bauchi",  # Dambam
    "AKK": "Bauchi",  # Gamawa
    "KAT": "Bauchi",  # Ganjuwa
    "GML": "Bauchi",  # Giade
    "JMR": "Bauchi",  # Jamaare
    "KKW": "Bauchi",  # Katagum
    "MSH": "Bauchi",  # Misau
    "NNR": "Bauchi",  # Ningi
    "SHR": "Bauchi",  # Shira
    "TFW": "Bauchi",  # Tafawa Balewa
    "TRO": "Bauchi",  # Toro
    "WRJ": "Bauchi",  # Warji
    "ZAK": "Bauchi",  # Zaki

    # ── Bayelsa ───────────────────────────────────────────
    "YEN": "Bayelsa",  # Yenagoa
    "KMR": "Bayelsa",  # Kolokuma / Opokuma
    "KMK": "Bayelsa",  # Sagbama
    "NEM": "Bayelsa",  # Nembe
    "GBB": "Bayelsa",  # Ogbia
    "SAG": "Bayelsa",  # Southern Ijaw
    "SPR": "Bayelsa",  # Brass
    "BRS": "Bayelsa",  # Ekeremor

    # ── Benue ─────────────────────────────────────────────
    "BEN": "Benue",   # Makurdi
    "PKG": "Benue",   # Gboko
    "GBK": "Benue",   # Vandeikya
    "MKD": "Benue",   # Katsina-Ala
    "OTU": "Benue",   # Otukpo
    "ADK": "Benue",   # Ado
    "AGT": "Benue",   # Agatu
    "ALE": "Benue",   # Apa
    "BRK": "Benue",   # Buruku
    "GUM": "Benue",   # Guma
    "GWR": "Benue",   # Gwer East / Gwer West
    "KND": "Benue",   # Konshisha
    "KWA": "Benue",   # Kwande
    "LGO": "Benue",   # Logo
    "ODZ": "Benue",   # Obi
    "OGW": "Benue",   # Ogbadibo
    "OKP": "Benue",   # Ohimini
    "TARv": "Benue",  # Tarka
    "UKM": "Benue",   # Ukum
    "USD": "Benue",   # Ushongo

    # ── Borno ─────────────────────────────────────────────
    "BAM": "Borno",  # Bama
    "BBU": "Borno",  # Biu
    "DAM": "Borno",  # Damboa
    "DKW": "Borno",  # Dikwa
    "HWL": "Borno",  # Hawul
    "MAI": "Borno",  # Maiduguri
    "MUG": "Borno",  # Monguno
    "ASK": "Borno",  # Askira / Uba
    "CHD": "Borno",  # Chibok
    "GGN": "Borno",  # Gubio
    "GZR": "Borno",  # Guzamala
    "JRE": "Borno",  # Jere
    "KAL": "Borno",  # Kala / Balge
    "KBB": "Borno",  # Kaga
    "KWY": "Borno",  # Kwaya Kusar
    "MFN": "Borno",  # Mafa
    "MRT": "Borno",  # Magumeri
    "NGZ": "Borno",  # Nganzai

    # ── Cross River ───────────────────────────────────────
    "DUK": "Cross River",  # Akamkpa
    "CAL": "Cross River",  # Calabar
    "IKM": "Cross River",  # Ikom
    "OBU": "Cross River",  # Obubra
    "UGE": "Cross River",  # Ugep (Yakurr)
    "AKP": "Cross River",  # Akpabuyo
    "BKL": "Cross River",  # Bakassi
    "BKR": "Cross River",  # Bekwarra
    "BND": "Cross River",  # Biase
    "ETG": "Cross River",  # Etung
    "OBN": "Cross River",  # Obudu
    "ODK": "Cross River",  # Odukpani

    # ── Delta ─────────────────────────────────────────────
    "ABH": "Delta",  # Aniocha North / Aniocha South
    "AGB": "Delta",  # Agbor (Ika North East / Ika South)
    "BMA": "Delta",  # Bomadi
    "BUR": "Delta",  # Burutu
    "DET": "Delta",  # Ethiope East / Ethiope West
    "DNB": "Delta",  # Ndokwa East / Ndokwa West
    "DSZ": "Delta",  # Isoko North / Isoko South
    "ASB": "Delta",  # Asaba (Oshimili North / Oshimili South)
    "WAR": "Delta",  # Warri North / Warri South / Warri South West
    "UGH": "Delta",  # Ughelli North / Ughelli South
    "SLG": "Delta",  # Sapele / Okpe
    "OKR": "Delta",  # Okpe
    "UKW": "Delta",  # Ukwuani
    "UVW": "Delta",  # Uvwie

    # ── Ebonyi ────────────────────────────────────────────
    "HKW": "Ebonyi",  # Afikpo North / Afikpo South
    "AFK": "Ebonyi",  # Afikpo
    "EZA": "Ebonyi",  # Ezza North / Ezza South
    "OHZ": "Ebonyi",  # Ohaukwu
    "ABI": "Ebonyi",  # Abakaliki
    "EBH": "Ebonyi",  # Ebonyi
    "IKW": "Ebonyi",  # Ikwo
    "ISN": "Ebonyi",  # Ishielu
    "OZZ": "Ebonyi",  # Izzi

    # ── Edo ───────────────────────────────────────────────
    "ABD": "Edo",  # Akoko-Edo
    "AFZ": "Edo",  # Egor
    "AGD": "Edo",  # Esan Central / Esan North East / Esan South East / Esan West
    "AUB": "Edo",  # Etsako Central / Etsako East / Etsako West
    "IGU": "Edo",  # Igueben
    "UBJ": "Edo",  # Ikpoba-Okha
    "UCH": "Edo",  # Orhionmwon
    "OKP": "Edo",  # Oredo / Uhunmwonde
    "OVB": "Edo",  # Owan East / Owan West

    # ── Ekiti ─────────────────────────────────────────────
    "EFY": "Ekiti",  # Ado Ekiti (Ekiti South West)
    "EAA": "Ekiti",  # Ekiti East
    "GED": "Ekiti",  # Gbonyin
    "IER": "Ekiti",  # Ido-Osi
    "KRE": "Ekiti",  # Ijero
    "MUE": "Ekiti",  # Ikere
    "TUN": "Ekiti",  # Ikole
    "YEK": "Ekiti",  # Ilejemeje
    "EKT": "Ekiti",  # Emure
    "MOB": "Ekiti",  # Moba
    "OYE": "Ekiti",  # Oye

    # ── Enugu ─────────────────────────────────────────────
    "AGN": "Enugu",  # Agwu
    "AGW": "Enugu",  # Awgu
    "BBG": "Enugu",  # Enugu East / Enugu North / Enugu South
    "ENU": "Enugu",  # Ezeagu
    "AWD": "Enugu",  # Igbo-Etiti / Igbo-Eze North / Igbo-Eze South
    "UDI": "Enugu",  # Isi-Uzo / Nkanu East / Nkanu West
    "NSK": "Enugu",  # Nsukka
    "UZO": "Enugu",  # Uzo-Uwani
    "OJI": "Enugu",  # Oji River

    # ── Abuja (FCT) ───────────────────────────────────────
    "ABC": "Abuja (FCT)",  # Abaji
    "ABJ": "Abuja (FCT)",  # Abuja Municipal Area Council (AMAC)
    "BWR": "Abuja (FCT)",  # Bwari
    "GWA": "Abuja (FCT)",  # Gwagwalada
    "KUJ": "Abuja (FCT)",  # Kuje
    "KWL": "Abuja (FCT)",  # Kwali
    "RBC": "Abuja (FCT)",  # (general FCT)
    "RSH": "Abuja (FCT)",  # (general FCT)
    "YAB": "Abuja (FCT)",  # (general FCT)

    # ── Gombe ─────────────────────────────────────────────
    "GME": "Gombe",  # Gombe
    "BKK": "Gombe",  # Akko
    "KMG": "Gombe",  # Kaltungo
    "NFD": "Gombe",  # Nafada
    "DBS": "Gombe",  # Dukku
    "BLN": "Gombe",  # Balanga
    "FNY": "Gombe",  # Funakaye
    "KKR": "Gombe",  # Kwami
    "SHM": "Gombe",  # Shomgom
    "YAM": "Gombe",  # Yamaltu / Deba

    # ── Imo ───────────────────────────────────────────────
    "WER": "Imo",   # Aboh Mbaise / Ahiazu Mbaise
    "ORL": "Imo",   # Orlu
    "OKI": "Imo",   # Okigwe
    "MGB": "Imo",   # Mbaitoli
    "KGE": "Imo",   # Ikeduru
    "NKR": "Imo",   # Nkwerre / Ngor Okpala
    "TTK": "Imo",   # Oru East / Oru West
    "UMD": "Imo",   # Owerri North / Owerri West / Owerri Municipal
    "EZN": "Imo",   # Ezinihitte
    "HJK": "Imo",   # Ihitte / Uboma
    "ISL": "Imo",   # Isiala Mbano
    "OGT": "Imo",   # Oguta
    "OHJ": "Imo",   # Ohaji / Egbema
    "ONJ": "Imo",   # Onuimo

    # ── Jigawa ────────────────────────────────────────────
    "BBR": "Jigawa",  # Biriniwa
    "BMW": "Jigawa",  # Birnin Kudu
    "DTU": "Jigawa",  # Dutse
    "HJA": "Jigawa",  # Hadejia
    "KZR": "Jigawa",  # Kazaure
    "RNG": "Jigawa",  # Ringim
    "GRL": "Jigawa",  # Garki
    "GWR": "Jigawa",  # Gagarawa
    "GZK": "Jigawa",  # Gumel
    "KYW": "Jigawa",  # Kiyawa
    "MKN": "Jigawa",  # Maigatari
    "MLR": "Jigawa",  # Malam Madori
    "MYM": "Jigawa",  # Miga
    "RNN": "Jigawa",  # Roni
    "SRN": "Jigawa",  # Sule Tankarkar
    "TKW": "Jigawa",  # Takai (Kano border shared)
    "YAK": "Jigawa",  # Yankwashi

    # ── Kaduna ────────────────────────────────────────────
    "KAD": "Kaduna",  # Kaduna North / Kaduna South
    "DKA": "Kaduna",  # Chikun
    "MKA": "Kaduna",  # Igabi
    "ZAR": "Kaduna",  # Zaria
    "TRN": "Kaduna",  # Soba
    "BNG": "Kaduna",  # Birnin Gwari
    "KAF": "Kaduna",  # Kaura
    "KCH": "Kaduna",  # Kachia
    "MGN": "Kaduna",  # Makarfi
    "SAB": "Kaduna",  # Sabon Gari
    "ZKW": "Kaduna",  # Zangon Kataf
    "GGM": "Kaduna",  # Giwa
    "JMK": "Kaduna",  # Jema'a
    "KBK": "Kaduna",  # Kudan
    "KUB": "Kaduna",  # Kubau
    "LRE": "Kaduna",  # Lere
    "TBN": "Kaduna",  # Kauru

    # ── Kano ──────────────────────────────────────────────
    "KAN": "Kano",  # Kano Municipal
    "KMC": "Kano",  # Kano Metropolitan
    "BKN": "Kano",  # Bunkure
    "DBT": "Kano",  # Dambatta
    "ABS": "Kano",  # Albasu
    "AJG": "Kano",  # Ajingi
    "BBJ": "Kano",  # Bagwai
    "BCH": "Kano",  # Bebeji
    "DAL": "Kano",  # Dala
    "DGW": "Kano",  # Dawakin Kudu / Dawakin Tofa
    "DKD": "Kano",  # Doguwa
    "DTA": "Kano",  # Dutse (shared — context decides)
    "DTF": "Kano",  # Fagge
    "WUD": "Kano",  # Warawa
    "GRN": "Kano",  # Garun Mallam
    "GWL": "Kano",  # Gwale
    "GWZ": "Kano",  # Gwarzo
    "KBB": "Kano",  # Kibiya
    "KGR": "Kano",  # Kiru
    "KNG": "Kano",  # Kumbotso
    "KRY": "Kano",  # Kunchi
    "MNJ": "Kano",  # Minjibir
    "NSR": "Kano",  # Nasarawa (Kano)
    "RNJ": "Kano",  # Rimin Gado
    "RRN": "Kano",  # Rogo
    "SBN": "Kano",  # Shanono
    "TRK": "Kano",  # Tarauni
    "TSY": "Kano",  # Tofa
    "TWR": "Kano",  # Tudun Wada
    "UNZ": "Kano",  # Ungogo
    "WDL": "Kano",  # Wudil

    # ── Katsina ───────────────────────────────────────────
    "BAT": "Katsina",  # Batagarawa
    "BKR": "Katsina",  # Bakori
    "BDU": "Katsina",  # Bindawa
    "BKY": "Katsina",  # Baure
    "DRA": "Katsina",  # Dandume
    "DSM": "Katsina",  # Daura
    "DNJ": "Katsina",  # Dutsi
    "KTN": "Katsina",  # Katsina
    "FNT": "Katsina",  # Funtua
    "CBR": "Katsina",  # Charanchi
    "DTM": "Katsina",  # Dutsin-Ma
    "INK": "Katsina",  # Ingawa
    "JBL": "Katsina",  # Jibia
    "KNK": "Katsina",  # Kafur
    "KGR": "Katsina",  # Kaita
    "KNK": "Katsina",  # Kankara
    "KNY": "Katsina",  # Kankia
    "KRY": "Katsina",  # Kurfi
    "KTS": "Katsina",  # Kusada
    "MNI": "Katsina",  # Mai'adua
    "MNS": "Katsina",  # Malumfashi
    "MNI": "Katsina",  # Mani
    "MRD": "Katsina",  # Mashi
    "MTS": "Katsina",  # Matazu
    "MUS": "Katsina",  # Musawa
    "RFD": "Katsina",  # Rimi
    "SDK": "Katsina",  # Sabuwa
    "SFN": "Katsina",  # Safana
    "SGR": "Katsina",  # Sandamu
    "ZNG": "Katsina",  # Zango

    # ── Kebbi ─────────────────────────────────────────────
    "BES": "Kebbi",  # Birnin Kebbi
    "BGD": "Kebbi",  # Bagudo
    "DKG": "Kebbi",  # Dandi
    "BRK": "Kebbi",  # Bunza
    "ARG": "Kebbi",  # Argungu
    "YUR": "Kebbi",  # Yauri
    "JEG": "Kebbi",  # Jega
    "ALR": "Kebbi",  # Aliero
    "FAZ": "Kebbi",  # Fakai
    "GWN": "Kebbi",  # Gwandu
    "KLB": "Kebbi",  # Kalgo
    "KNK": "Kebbi",  # Koko / Besse
    "MSK": "Kebbi",  # Maiyama
    "NGD": "Kebbi",  # Ngaski
    "SKK": "Kebbi",  # Sakaba
    "SHG": "Kebbi",  # Shanga
    "SRZ": "Kebbi",  # Suru
    "WRM": "Kebbi",  # Wasagu / Danko
    "ZRU": "Kebbi",  # Zuru

    # ── Kogi ──────────────────────────────────────────────
    "BAS": "Kogi",  # Bassa
    "DAH": "Kogi",  # Dekina
    "DKN": "Kogi",  # Ibaji
    "LKJ": "Kogi",  # Lokoja
    "KBA": "Kogi",  # Kabba / Bunu
    "ANC": "Kogi",  # Ankpa
    "OKN": "Kogi",  # Okehi
    "AJK": "Kogi",  # Ajaokuta
    "ADF": "Kogi",  # Adavi
    "IJM": "Kogi",  # Ijumu
    "KOT": "Kogi",  # Koto Karifi
    "MGN": "Kogi",  # Mopa-Muro
    "OFN": "Kogi",  # Ofu
    "OLM": "Kogi",  # Ogori / Magongo
    "OPD": "Kogi",  # Olamaboro
    "YAG": "Kogi",  # Yagba East / Yagba West

    # ── Kwara ─────────────────────────────────────────────
    "AFN": "Kwara",  # Asa
    "ILR": "Kwara",  # Ilorin East / Ilorin South / Ilorin West
    "MUN": "Kwara",  # Moro
    "OFF": "Kwara",  # Offa
    "KEY": "Kwara",  # Ekiti (Kwara)
    "LFM": "Kwara",  # Ifelodun
    "EDU": "Kwara",  # Edu
    "GBJ": "Kwara",  # Irepodun
    "IJR": "Kwara",  # Isin
    "KAI": "Kwara",  # Kaiama
    "OKE": "Kwara",  # Oke-Ero
    "PTG": "Kwara",  # Pategi
    "SLT": "Kwara",  # Oyun (Ilofa)

    # ── Lagos ─────────────────────────────────────────────
    "AAA": "Lagos",  # (general Lagos)
    "AKD": "Lagos",  # Agege
    "AGL": "Lagos",  # Ajeromi-Ifelodun
    "APP": "Lagos",  # Apapa
    "BDG": "Lagos",  # Badagry
    "EKY": "Lagos",  # Epe
    "EPE": "Lagos",  # Epe
    "FKJ": "Lagos",  # Ikorodu
    "FST": "Lagos",  # Surulere
    "GGE": "Lagos",  # Ikeja
    "JJJ": "Lagos",  # (general Lagos)
    "KJA": "Lagos",  # Kosofe
    "KRD": "Lagos",  # Lagos Island
    "KSF": "Lagos",  # Lagos Mainland
    "KTU": "Lagos",  # Mushin
    "LND": "Lagos",  # Eti-Osa
    "LSD": "Lagos",  # Alimosho
    "LSR": "Lagos",  # Oshodi-Isolo
    "MUS": "Lagos",  # Mushin (alt)
    "SMK": "Lagos",  # Somolu
    "OJO": "Lagos",  # Ojo
    "IFO": "Lagos",  # Ifako-Ijaiye
    "ABL": "Lagos",  # Amuwo-Odofin

    # ── Nasarawa ──────────────────────────────────────────
    "LFA": "Nasarawa",  # Lafia
    "KFF": "Nasarawa",  # Keffi
    "AKW": "Nasarawa",  # Akwanga
    "WAM": "Nasarawa",  # Wamba
    "KEG": "Nasarawa",  # Keana
    "AWT": "Nasarawa",  # Awe
    "DMA": "Nasarawa",  # Doma
    "KKR": "Nasarawa",  # Kokona
    "NSW": "Nasarawa",  # Nasarawa (town)
    "NSE": "Nasarawa",  # Nasarawa Egon
    "OBU": "Nasarawa",  # Obi (Nasarawa)
    "TRT": "Nasarawa",  # Toto

    # ── Niger ─────────────────────────────────────────────
    "AGA": "Niger",  # Agaie
    "AGR": "Niger",  # Agwara
    "BDA": "Niger",  # Bida
    "PAK": "Niger",  # Paikoro
    "MNA": "Niger",  # Minna
    "SUL": "Niger",  # Suleja
    "KNT": "Niger",  # Kontagora
    "LAP": "Niger",  # Lapai
    "NAG": "Niger",  # Magama
    "BOS": "Niger",  # Borgu
    "CHC": "Niger",  # Chanchaga
    "EDI": "Niger",  # Edati
    "GBR": "Niger",  # Gbako
    "GRK": "Niger",  # Gurara
    "KTG": "Niger",  # Katcha
    "KWM": "Niger",  # Mashegu
    "MAR": "Niger",  # Mariga
    "MOP": "Niger",  # Mokwa
    "MRT": "Niger",  # Munya
    "RAF": "Niger",  # Rafi
    "RJY": "Niger",  # Rijau
    "SHG": "Niger",  # Shiroro
    "WUS": "Niger",  # Wushishi

    # ── Ogun ──────────────────────────────────────────────
    "AAB": "Ogun",  # Abeokuta North / Abeokuta South
    "ABG": "Ogun",  # Ado-Odo / Ota
    "DED": "Ogun",  # Ewekoro
    "DGB": "Ogun",  # Ifo
    "AKM": "Ogun",  # Ijebu East / Ijebu North / Ijebu North East / Ijebu Ode
    "SGM": "Ogun",  # Sagamu
    "JBD": "Ogun",  # Obafemi-Owode
    "TTN": "Ogun",  # Odeda
    "WDE": "Ogun",  # Odogbolu
    "TRE": "Ogun",  # Ikenne
    "SMG": "Ogun",  # Imeko-Afon
    "GBG": "Ogun",  # Remo North
    "YWY": "Ogun",  # Yewa North / Yewa South

    # ── Ondo ──────────────────────────────────────────────
    "DEK": "Ondo",  # Akure North / Akure South
    "AKR": "Ondo",  # Akoko North East / Akoko North West / Akoko South East / Akoko South West
    "OND": "Ondo",  # Ondo East / Ondo West
    "OWO": "Ondo",  # Owo
    "KAA": "Ondo",  # Ese-Odo
    "REE": "Ondo",  # Idanre
    "FFN": "Ondo",  # Ifedore
    "SUA": "Ondo",  # Ilaje
    "IRJ": "Ondo",  # Ile-Oluji / Okeigbo
    "OKT": "Ondo",  # Odigbo
    "OKG": "Ondo",  # Okitipupa

    # ── Osun ──────────────────────────────────────────────
    "AAW": "Osun",  # Atakumosa East / Atakumosa West
    "BDS": "Osun",  # Boripe
    "DTN": "Osun",  # Boluwaduro
    "PMD": "Osun",  # Aiyedire
    "OSG": "Osun",  # Osogbo
    "LES": "Osun",  # Ilesha East / Ilesha West
    "EDE": "Osun",  # Ede North / Ede South
    "GBN": "Osun",  # Iwo
    "FEE": "Osun",  # Ife North / Ife South / Ife East / Ife Central
    "SGB": "Osun",  # Olorunda
    "AYD": "Osun",  # Ayedaade
    "EJG": "Osun",  # Ejigbo
    "GBG": "Osun",  # Egbedore
    "IRE": "Osun",  # Irewole / Isokan
    "OBK": "Osun",  # Obokun
    "ODG": "Osun",  # Odo-Otin
    "OLR": "Osun",  # Ola-Oluwa
    "ORT": "Osun",  # Orolu

    # ── Oyo ───────────────────────────────────────────────
    "AGG": "Oyo",  # Afijio
    "AJW": "Oyo",  # Akinyele
    "BDJ": "Oyo",  # Ibadan North / Ibadan North East / Ibadan North West / Ibadan South East / Ibadan South West
    "DDA": "Oyo",  # Egbeda
    "IBA": "Oyo",  # Ibarapa Central / Ibarapa East / Ibarapa North
    "IBZ": "Oyo",  # Ido
    "NRK": "Oyo",  # Irepo
    "YEM": "Oyo",  # Iseyin
    "MAP": "Oyo",  # Itesiwaju
    "LUY": "Oyo",  # Iwajowa
    "AYE": "Oyo",  # Kajola
    "GNN": "Oyo",  # Lagelu
    "OGO": "Oyo",  # Ogbomoso North / Ogbomoso South
    "OKK": "Oyo",  # Ogo-Oluwa
    "OLY": "Oyo",  # Oluyole
    "ONO": "Oyo",  # Ona-Ara
    "ORP": "Oyo",  # Orelope
    "ORF": "Oyo",  # Ori-Ire
    "OYO": "Oyo",  # Oyo East / Oyo West
    "SRK": "Oyo",  # Saki East / Saki West
    "SRR": "Oyo",  # Surulere (Oyo)

    # ── Plateau ───────────────────────────────────────────
    "BLD": "Plateau",  # Barkin Ladi
    "DMA": "Plateau",  # Bokkos
    "DNG": "Plateau",  # Bassa (Plateau)
    "PBB": "Plateau",  # Pankshin
    "PKN": "Plateau",  # Kanam
    "PTT": "Plateau",  # Kanke
    "JOS": "Plateau",  # Jos East / Jos North / Jos South
    "BUK": "Plateau",  # Langtang North / Langtang South
    "QAN": "Plateau",  # Quaan Pan
    "LAN": "Plateau",  # Mangu
    "MKN": "Plateau",  # Mikang
    "RYM": "Plateau",  # Riyom
    "SHN": "Plateau",  # Shendam
    "WAS": "Plateau",  # Wase

    # ── Rivers ────────────────────────────────────────────
    "ABM": "Rivers",  # Abua / Odual
    "ABU": "Rivers",  # Ahoada East / Ahoada West
    "AFM": "Rivers",  # Akuku-Toru
    "AHD": "Rivers",  # Andoni
    "DBU": "Rivers",  # Asari-Toru
    "PHC": "Rivers",  # Port Harcourt
    "AHO": "Rivers",  # Bonny
    "BGM": "Rivers",  # Degema
    "BNY": "Rivers",  # Eleme
    "DEG": "Rivers",  # Emuoha
    "ELE": "Rivers",  # Etche
    "KNM": "Rivers",  # Gokana
    "OBK": "Rivers",  # Ikwerre
    "RUM": "Rivers",  # Khana
    "NCH": "Rivers",  # Obio-Akpor
    "GOK": "Rivers",  # Ogba / Egbema / Ndoni
    "BRR": "Rivers",  # Ogu / Bolo
    "OML": "Rivers",  # Omuma
    "OPK": "Rivers",  # Opobo / Nkoro
    "OYG": "Rivers",  # Oyigbo
    "TML": "Rivers",  # Tai

    # ── Sokoto ────────────────────────────────────────────
    "BDN": "Sokoto",  # Binji
    "BUG": "Sokoto",  # Bodinga
    "DGS": "Sokoto",  # Dange-Shuni
    "SOK": "Sokoto",  # Sokoto North / Sokoto South
    "GWD": "Sokoto",  # Gada
    "TBD": "Sokoto",  # Goronyo
    "SRZ": "Sokoto",  # Gudu
    "KWE": "Sokoto",  # Gwadabawa
    "ILL": "Sokoto",  # Illela
    "ISH": "Sokoto",  # Isa
    "KBB": "Sokoto",  # Kebbe
    "KND": "Sokoto",  # Kware
    "RBH": "Sokoto",  # Rabah
    "SKN": "Sokoto",  # Sabon Birni
    "SHG": "Sokoto",  # Shagari
    "SLM": "Sokoto",  # Silame
    "TMB": "Sokoto",  # Tambuwal
    "TGZ": "Sokoto",  # Tangaza
    "TRZ": "Sokoto",  # Tureta
    "WMK": "Sokoto",  # Wamako
    "WRR": "Sokoto",  # Wurno
    "YAB": "Sokoto",  # Yabo

    # ── Taraba ────────────────────────────────────────────
    "BAL": "Taraba",  # Ardo-Kola
    "BBB": "Taraba",  # Bali
    "DGA": "Taraba",  # Donga
    "JAL": "Taraba",  # Gashaka
    "MUT": "Taraba",  # Gassol
    "GKA": "Taraba",  # Ibi
    "WUK": "Taraba",  # Jalingo
    "ZNG": "Taraba",  # Karim-Lamido
    "KRN": "Taraba",  # Kurmi
    "LDN": "Taraba",  # Lau
    "SEV": "Taraba",  # Sardauna
    "TKW": "Taraba",  # Takum
    "UNG": "Taraba",  # Ussa
    "WKN": "Taraba",  # Wukari
    "YRN": "Taraba",  # Yorro
    "ZAK": "Taraba",  # Zing

    # ── Yobe ──────────────────────────────────────────────
    "DPH": "Yobe",  # Bade
    "DTR": "Yobe",  # Bursari
    "PKM": "Yobe",  # Damaturu
    "BUN": "Yobe",  # Fika
    "GUA": "Yobe",  # Fune
    "NGR": "Yobe",  # Geidam
    "FKA": "Yobe",  # Gujba
    "MCK": "Yobe",  # Gulani
    "JKM": "Yobe",  # Jakusko
    "KJY": "Yobe",  # Karasuwa
    "MRT": "Yobe",  # Machina
    "NGR": "Yobe",  # Nangere
    "POT": "Yobe",  # Potiskum
    "TRM": "Yobe",  # Tarmuwa
    "YBE": "Yobe",  # Yunusari
    "YSF": "Yobe",  # Yusufari

    # ── Zamfara ───────────────────────────────────────────
    "GUS": "Zamfara",  # Anka
    "KNR": "Zamfara",  # Bakura
    "MRD": "Zamfara",  # Birnin Magaji / Kiyaw
    "ANR": "Zamfara",  # Bukkuyum
    "TSF": "Zamfara",  # Bungudu
    "ZRM": "Zamfara",  # Gummi
    "GSR": "Zamfara",  # Gusau
    "KYB": "Zamfara",  # Kaura Namoda
    "MRS": "Zamfara",  # Maradun
    "MTA": "Zamfara",  # Maru
    "SFN": "Zamfara",  # Shinkafi
    "TLT": "Zamfara",  # Talata Mafara
    "TSB": "Zamfara",  # Tsafe
    "ZRF": "Zamfara",  # Zurmi
}


def get_state_from_lga_prefix(plate_number: str) -> str:
    """
    Extract the first 3 characters from a plate number and look up
    the corresponding state from the LGA_MAP.

    Accepts formats:
        'ABC123XY'   → prefix = 'ABC'
        'ABC-123-XY' → prefix = 'ABC'

    Returns the state name string, or 'Unknown' if not found.
    """
    # Strip dashes and spaces, then uppercase
    clean = plate_number.replace("-", "").replace(" ", "").upper()
    prefix = clean[:3]
    return LGA_MAP.get(prefix, "Unknown")


def get_state_from_text(ocr_text: str) -> str:
    """
    Match OCR text against known state keywords.
    Returns the state name string, or 'Unknown' if not found.
    """
    import difflib
    text = ocr_text.upper().replace(" ", "").replace("-", "")
    for keyword, state in NIGERIA_STATES.items():
        if keyword in text:
            return state
    matches = difflib.get_close_matches(
        text, list(NIGERIA_STATES.keys()), n=1, cutoff=0.8
    )
    if matches:
        return NIGERIA_STATES[matches[0]]
    return "Unknown"