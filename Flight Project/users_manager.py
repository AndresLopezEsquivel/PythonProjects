import os
import requests

USERS_SHEET_ENDPOINT = os.environ.get("USERS_SHEET_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_HEADERS = {"Authorization": SHEETY_TOKEN}


class UsersManager:

    def get_users_emails(self):
        current_users_data = requests.get(url=USERS_SHEET_ENDPOINT, headers=SHEETY_HEADERS).json()["users"]
        users_emails = [user_data["email"] for user_data in current_users_data]
        return users_emails
