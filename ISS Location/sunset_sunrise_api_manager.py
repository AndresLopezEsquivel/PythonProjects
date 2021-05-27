import requests


def get_json(end_point, parameters):
    response = requests.get(url=end_point, params=parameters)
    response.raise_for_status()
    return response.json()


class SunsetSunriseApiManager:

    def __init__(self, end_point, parameters):
        self.end_point = end_point
        self.parameters = parameters

    def get_sunset_sunrise_hours(self):
        json = get_json(end_point=self.end_point, parameters=self.parameters)
        print(json)