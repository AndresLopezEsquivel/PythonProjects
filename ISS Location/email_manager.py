import smtplib as smtp

GMAIL_SMTP = "smtp.gmail.com"
SENDER = ""
SENDER_PASSWORD = ""


class EmailManager:

    def __init__(self, subject, message, recipient_email):
        self.complete_message = f"Subject: {subject} \n\n {message}"
        self.recipient_email = recipient_email

    def send_email(self):
        with smtp.SMTP(GMAIL_SMTP, port=587) as connection:
            # TLS: Transport Layer Security
            connection.starttls()
            connection.login(user=SENDER, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER,
                                to_addrs=self.recipient_email,
                                msg=self.complete_message)
            print("Email successfully sent :)")
