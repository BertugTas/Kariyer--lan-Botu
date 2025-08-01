# sms_bildirim.py

from twilio.rest import Client

# 👇 Buraya kendi Twilio bilgilerini gir!
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
FROM_PHONE = "+1XXXXXXXXXX"     # Twilio numaran
TO_PHONE = "+90XXXXXXXXXX"      # SMS gönderilecek kişi

def sms_gonder(mesaj):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=mesaj,
        from_=FROM_PHONE,
        to=TO_PHONE
    )
