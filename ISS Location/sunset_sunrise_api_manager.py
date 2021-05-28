import requests


def get_json(end_point, parameters):
    response = requests.get(url=end_point, params=parameters)
    response.raise_for_status()
    json = response.json()
    return json


class SunsetSunriseApiManager:

    def __init__(self, end_point, parameters):
        self.end_point = end_point
        self.parameters = parameters

    def get_sunrise_sunset_hours(self):
        json = get_json(end_point=self.end_point, parameters=self.parameters)
        sunrise_hour = json["results"]["sunrise"].split("T")[1].split(":")[0]
        sunset_hour = json["results"]["sunset"].split("T")[1].split(":")[0]
        return int(sunrise_hour), int(sunset_hour)
