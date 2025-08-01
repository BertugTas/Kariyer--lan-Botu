# bot_runner.py

import schedule
import time
from kariyer_bot import run_playwright_kariyer_bot
from ilan_kontrol import yeni_ilanlari_bul, ilanlari_kaydet
from sms_bildirim import sms_gonder

def kontrol_et():
    print("📡 Yeni ilan kontrolü başlatıldı...")
    yeni_liste = run_playwright_kariyer_bot()
    farklar = yeni_ilanlari_bul(yeni_liste)

    if farklar:
        mesaj = f"📢 Yeni ilan(lar) bulundu!\n\n"
        for ilan in farklar:
            mesaj += f"{ilan['baslik']}\n{ilan['link']}\n\n"
        sms_gonder(mesaj)
        ilanlari_kaydet(yeni_liste)
        print("SMS gönderildi.")
    else:
        print("Yeni ilan yok.")

# Her 5 dakikada bir çalıştır:
schedule.every(5).minutes.do(kontrol_et)

print("Bot çalışıyor... Ctrl+C ile durdur.")
while True:
    schedule.run_pending()
    time.sleep(1)
