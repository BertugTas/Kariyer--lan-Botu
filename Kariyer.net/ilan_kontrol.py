# ilan_kontrol.py

import json
import os

DOSYA = "ilanlar.json"

def eski_ilanlari_yukle():
    if not os.path.exists(DOSYA):
        return []
    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)

def yeni_ilanlari_bul(yeniler):
    eski_linkler = [i["link"] for i in eski_ilanlari_yukle()]
    return [i for i in yeniler if i["link"] not in eski_linkler]

def ilanlari_kaydet(yeniler):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(yeniler, f, ensure_ascii=False, indent=2)
