# 🧪 Kariyer.net Kimya Öğretmeni İlan Takip Botu

Bu Python tabanlı bot, [kariyer.net](https://kariyer.net) sitesinde Mersin bölgesinde yayınlanan **Kimya Öğretmeni** ilanlarını takip eder. Yeni ilan tespit edildiğinde SMS ile haber verir.

## 🚀 Özellikler

- Kariyer.net üzerinde belirli anahtar kelime ve şehir filtrelerine göre ilanları kontrol eder.
- Yeni ilan eklenmişse `.json` dosyasına kaydeder.
- Twilio kullanarak SMS bildirimi gönderir.
- Her 5 dakikada bir otomatik çalışacak şekilde zamanlanmıştır.
- PythonAnywhere gibi platformlara yüklenerek 7/24 açık tutulabilir.

---

## 🔧 Gereksinimler

```bash
Python 3.10+ önerilir
```

### 📦 Kurulması gereken kütüphaneler:

```bash
pip install playwright twilio schedule
playwright install
```

---

## 📁 Proje Yapısı

```
kariyer-bot/
│
├── bot_runner.py         # Ana zamanlayıcı (5 dakikada bir kontrol)
├── kariyer_bot.py        # Kariyer.net scraping işlemi
├── ilan_kontrol.py       # Yeni ilanları karşılaştırır/kaydeder
├── sms_bildirim.py       # Twilio SMS gönderimi
├── sms_test.py           # Twilio test mesajı
├── ilanlar.json          # (Oluşturulduğunda) önceki ilanların listesi
```

---

## ⚙️ Kullanım

### 1. Twilio Ayarları

`sms_bildirim.py` içinde aşağıdaki bilgileri doldur:

```python
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
FROM_PHONE = "+1XXXXXXXXXX"     # Twilio numaran
TO_PHONE = "+90XXXXXXXXXX"      # SMS gönderilecek kişi
```

> ⚠️ Trial hesaplarda sadece doğrulanmış numaralara SMS gider.

### 2. Test Et

```bash
python sms_test.py
```

### 3. Botu çalıştır

```bash
python bot_runner.py
```

---

## ☁️ Bulutta Çalıştırmak

PythonAnywhere veya Replit gibi platformlara yüklenerek bilgisayar açık olmasa da çalışabilir.

---

## 📜 Lisans

MIT License
