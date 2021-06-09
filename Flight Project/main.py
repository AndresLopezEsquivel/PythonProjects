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
