import requests


def get_json(end_point):
    response = requests.get(url=end_point)
    response.raise_for_status()
    return response.json()


class IssApiManager:

    def __init__(self, end_point):
        self.end_point = end_point

    def get_iss_coordinates(self):
        json = get_json(end_point=self.end_point)
        latitude = float(json["iss_position"]["latitude"])
        longitude = float(json["iss_position"]["longitude"])
        return latitude, longitude
