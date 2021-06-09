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

    def set_destination_data(self, destination_data):
        self.destination_data = destination_data

    def update_sheet(self):
        for city in self.destination_data:
            city_id = city["id"]
            city_iata_code = city["iataCode"]
            self.update_city_iata_code(city_id=city_id,
                                       iata_code=city_iata_code)

    def update_city_iata_code(self, city_id, iata_code):
        request_body = {
            "price": {
                "iataCode": iata_code
            }
        }

        request_endpoint = f"{SHEETY_ENDPOINT}/{city_id}"

        response = requests.put(url=request_endpoint,
                                json=request_body,
                                headers=SHEETY_HEADERS)
        print(f"Updating city IATA code: {response.text}")
