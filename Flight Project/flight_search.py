import os
import requests

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name: str) -> str:
        headers = {"apiKey": TEQUILA_API_KEY}
        body = {"term": city_name}
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        response = requests.get(url=endpoint,
                            params=body,
                            headers=headers)
        data = response.json()
        iata_code = data["locations"][0]["code"]
        return iata_code
