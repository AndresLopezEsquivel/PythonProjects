from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from pprint import pprint
import os
import requests

ORIGIN_IATA_CODE = "LON"
MIN_NIGHTS_IN_DST = 7
MAX_NIGHTS_IN_DST = 28

sheet_manager = DataManager()
flight_search_manager = FlightSearch()
sheet_data = sheet_manager.get_destination_data()

print(sheet_data)

for city in sheet_data:
    if not city["iataCode"]:
        city["iataCode"] = flight_search_manager.get_destination_code(city["city"])
        city_id = city["id"]
        city_iata_code = city["iataCode"]
        sheet_manager.update_city_iata_code(city_id=city_id,
                                            iata_code=city_iata_code)
    origin_city_code = ORIGIN_IATA_CODE
    destination_city_code = city["iataCode"]
    now = datetime.now()
    from_time = now.date().strftime("%d/%m/%Y")
    to_time = (now.date() + timedelta(days=180)).strftime("%d/%m/%Y")
    min_nights_in_dst = MIN_NIGHTS_IN_DST
    max_nights_in_dst = MAX_NIGHTS_IN_DST
    flight_data = flight_search_manager.check_for_flights(origin_city_code=origin_city_code,
                                                          destination_city_code=destination_city_code,
                                                          from_time=from_time,
                                                          to_time=to_time,
                                                          min_nights_in_dst=min_nights_in_dst,
                                                          max_nights_in_dst=max_nights_in_dst)
    print(f"{flight_data.destination_city}: £{flight_data.price}")

sheet_manager.set_destination_data(destination_data=sheet_data)
