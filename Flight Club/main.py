import os
import requests

SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
USERS_SHEET_ENDPOINT = os.environ.get("USERS_SHEET_ENDPOINT")
headers = {"Authorization" : SHEET_TOKEN}

# structure of the json received
# {'users': [{'firstName': 'Name', 'lastName': 'Last name', 'email': 'email', 'id': #}]}
current_users_data = requests.get(url=USERS_SHEET_ENDPOINT, headers=headers).json()["users"]
users_emails = [user_data["email"] for user_data in current_users_data]

print("Welcome to Andres' Flight Club.")
print("We find the best flight deals and email you.")
print("= = = = = = = = = =")
user_first_name = input("What is your first name? ")
user_last_name = input("What is your last name? ")
user_email = input("What is your email? ")

if not (user_email in users_emails):
    new_user_data = {
        "user": {
            "firstName": user_first_name,
            "lastName": user_last_name,
            "email": user_email
        }
    }
    response = requests.post(url=USERS_SHEET_ENDPOINT,
                             json=new_user_data,
                             headers=headers)
    print(f"Message from Sheety: {response.text}")
else:
    print("The email entered already exists in our database.")