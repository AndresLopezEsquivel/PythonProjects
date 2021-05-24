import json


class PasswordDataManager:

    def __init__(self, passwords_data_file_path):
        self.passwords_data_file_path = passwords_data_file_path

    def website_password_exists(self, website_searched):
        try:
            with open(self.passwords_data_file_path, "r") as passwords_file:
                passwords_data = json.load(passwords_file)
        except FileNotFoundError:
            return False
        else:
            if website_searched in passwords_data:
                return True
            else:
                return False

    def get_website_password(self, website_searched):
        with open(self.passwords_data_file_path, "r") as passwords_file:
            passwords_data = json.load(passwords_file)
            return passwords_data[website_searched]

    def add_new_password(self, new_password_data):
        try:
            with open(self.passwords_data_file_path, "r") as passwords_file:
                # passwords_data is a dictionary
                passwords_data = json.load(passwords_file)
        except FileNotFoundError:
            with open(self.passwords_data_file_path, "w") as passwords_file:
                json.dump(new_password_data, passwords_file, indent=4)
        else:
            passwords_data.update(new_password_data)
            with open(self.passwords_data_file_path, "w") as data_file:
                json.dump(passwords_data, data_file, indent=4)
