import os
import smtplib as smtp
from twilio.rest import Client

TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
RECIPIENT_PHONE_NUMBER = os.environ.get("RECIPIENT_PHONE_NUMBER")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

GMAIL_SMTP = "smtp.gmail.com"
SENDER = os.environ.get("SENDER")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message: str):
        message = self.client.messages.create(body=message,
                                              from_=TWILIO_PHONE_NUMBER,
                                              to=RECIPIENT_PHONE_NUMBER)
        print(message.sid)

    def send_email(self, recipient_email, message: str):
        subject = f"Subject: A NEW FLIGHT DEAL APPEARED!"
        final_message = f"{subject} \n\n {message}"
        with smtp.SMTP(GMAIL_SMTP, port=587) as connection:
            # TLS: Transport Layer Security
            connection.starttls()
            connection.login(user=SENDER, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER,
                                to_addrs=recipient_email,
                                msg=final_message)
