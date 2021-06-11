import os
import requests
from flight_data import FlightData

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


def get_data(endpoint, body, headers):
    response = requests.get(url=endpoint,
                            params=body,
                            headers=headers)
    return response.json()


class FlightSearch:

    def get_destination_code(self, city_name: str) -> str:
        body = {"term": city_name}
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apiKey": TEQUILA_API_KEY}
        data = get_data(endpoint=endpoint,
                        body=body,
                        headers=headers)
        iata_code = data["locations"][0]["code"]
        return iata_code

    def check_for_flights(self, origin_city_code: str,
                          destination_city_code: str,
                          from_time: str,
                          to_time: str,
                          min_nights_in_dst: int,
                          max_nights_in_dst: int):
        endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        body_request = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": min_nights_in_dst,
            "nights_in_dst_to": max_nights_in_dst
        }
        headers = {"apiKey": TEQUILA_API_KEY}
        response = get_data(endpoint=endpoint,
                            body=body_request,
                            headers=headers)
        data = response["data"][0]
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
