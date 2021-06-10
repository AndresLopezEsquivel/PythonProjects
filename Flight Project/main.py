from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import os
import requests

sheet_manager = DataManager()
flight_search_manager = FlightSearch()
sheet_data = sheet_manager.get_destination_data()

for city in sheet_data:
    if not city["iataCode"]:
        city["iataCode"] = flight_search_manager.get_destination_code(city["city"])
        city_id = city["id"]
        city_iata_code = city["iataCode"]
        sheet_manager.update_city_iata_code(city_id=city_id,
                                            iata_code=city_iata_code)

sheet_manager.set_destination_data(destination_data=sheet_data)

"""
iata_codes = ["PAR"]

headers_request = {
    "apiKey": ""
}

endpoint = "https://tequila-api.kiwi.com/v2/search"

date_from = datetime.now().date().strftime("%d/%m/%Y")

date_to = (datetime.now().date() + timedelta(days=180)).strftime("%d/%m/%Y")

nights_in_dst_from = 7

nights_in_dst_to = 28

for iata_code in iata_codes:
    body_request = {
        "fly_from": "LON",
        "fly_to": iata_code,
        "date_from": date_from,
        "date_to": date_to,
        "nights_in_dst_from": nights_in_dst_from,
        "nights_in_dst_to": nights_in_dst_to
    }
    response = requests.get(url=endpoint,
                            params=body_request,
                            headers=headers_request)

    data = response.json()["data"][0]

    pprint.pprint(data)

    price = f"{data['price']} €"

    from_date = data["local_arrival"].split("T")[0]

    date = from_date.split("-")

    to_date = datetime(year=int(date[0]), month=int(date[1]), day=int(date[2])) + timedelta(days=int(data["nightsInDest"]))

    print(f"Price: {price}")

    print(f"From: {from_date}")

    print(f"To: {to_date.date()}")
"""