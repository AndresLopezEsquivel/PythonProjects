import os
import requests

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_HEADERS = {"Authorization": SHEETY_TOKEN}


class DataManager:

    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        sheet_data = requests.get(url=SHEETY_ENDPOINT,
                                  headers=SHEETY_HEADERS).json()["prices"]
        self.destination_data = sheet_data
        return self.destination_data

    def update_sheet(self):
        for city in self.destination_data:
            sheet_request_body = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_request_endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"

            sheet_response = requests.put(url=put_request_endpoint,
                                          json=sheet_request_body,
                                          headers=SHEETY_HEADERS)
