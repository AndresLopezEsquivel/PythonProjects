from pprint import pprint
import os
import requests

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

sheety_headers = {
    "Authorization": SHEETY_TOKEN
}

sheet_data = requests.get(url=SHEETY_ENDPOINT,
                          headers=sheety_headers).json()["prices"]

for city in sheet_data:
    if not city["iataCode"]:
        city["iataCode"] = "TESTING"

for city in sheet_data:

    sheety_request_body = {
        "price": {
            "iataCode": city["iataCode"]
        }
    }

    put_request_endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"

    sheety_response = requests.put(url=put_request_endpoint,
                                   json=sheety_request_body,
                                   headers=sheety_headers)

    print(sheety_response.text)