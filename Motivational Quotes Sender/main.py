"""
Send motivational quotes to your friends on a specific day of the week
0 - Monday
1 - Thursday
2 - Wednesday
3 - Tuesday
4 - Friday
5 - Saturday
6 - Sunday
"""

import datetime as dt
import smtplib as smtp
import random as rd

QUOTES_FILE_PATH = "./quotes.txt"
GMAIL_SMTP = "smtp.gmail.com"
SENDER = ""
SENDER_PASSWORD = ""
RECIPIENT = ""

with open(QUOTES_FILE_PATH) as quotes_file:
    quotes = quotes_file.readlines()

now = dt.datetime.now()
day = now.weekday()

if day == 2:
    quote_of_the_day = rd.choice(quotes)
else:
    quote_of_the_day = ""

subject = "Subject: Quote of the day"
message = f"{subject} \n\n {quote_of_the_day}"

with smtp.SMTP(GMAIL_SMTP, port=587) as connection:
    # TLS: Transport Layer Security
    connection.starttls()
    connection.login(user=SENDER, password=SENDER_PASSWORD)
    connection.sendmail(from_addr=SENDER, to_addrs=RECIPIENT, msg=message)


