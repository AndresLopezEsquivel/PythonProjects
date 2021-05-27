import datetime as dt
import random as r
import smtplib as smtp
import pandas as p

BIRTHDAYS_DATA_FILE_PATH = "./birthdays.csv"
NAME_COLUMN = "name"
EMAIL_COLUMN = "email"
YEAR_COLUMN = "year"
MONTH_COLUMN = "month"
DAY_COLUMN = "day"
LETTERS_FILE_PATHS = ["./letter_templates/letter_1.txt",
                      "./letter_templates/letter_2.txt",
                      "./letter_templates/letter_3.txt"]
LETTER_NAME_FIELD = "[NAME]"
GMAIL_SMTP = "smtp.gmail.com"
SENDER = ""
SENDER_PASSWORD = ""
birthdays_data_file_exists = True


def write_letter(person_name):
    letter_file_path = r.choice(LETTERS_FILE_PATHS)
    try:
        with open(letter_file_path) as letter_file:
            letter = letter_file.read().replace(LETTER_NAME_FIELD, person_name)
    except FileNotFoundError:
        letter = f"Happy Birthday {person_name}."
    return letter


def send_email(person_name, recipient_email):
    subject = f"Subject: Happy Birthday {person_name}!"
    message = f"{subject} \n\n {write_letter(person_name)}"
    print(message)
    with smtp.SMTP(GMAIL_SMTP, port=587) as connection:
        # TLS: Transport Layer Security
        connection.starttls()
        connection.login(user=SENDER, password=SENDER_PASSWORD)
        connection.sendmail(from_addr=SENDER,
                            to_addrs=recipient_email,
                            msg=message)


try:
    birthdays_data_frame = p.read_csv(BIRTHDAYS_DATA_FILE_PATH)
except FileNotFoundError:
    print(f"Sorry, {BIRTHDAYS_DATA_FILE_PATH} does not exist.")
    birthdays_data_file_exists = False

if birthdays_data_file_exists:
    today = dt.datetime.now()
    current_month = today.month
    current_day = today.day
    # [{"name": string , "email": string, "year": int, "month": int, "day": int}, ...]
    birthdays_data = birthdays_data_frame.to_dict(orient="records")
    for data in birthdays_data:
        is_their_birthday = data[MONTH_COLUMN] == current_month and data[DAY_COLUMN] == current_day
        if is_their_birthday:
            name = data[NAME_COLUMN]
            email = data[EMAIL_COLUMN]
            send_email(name, email)

