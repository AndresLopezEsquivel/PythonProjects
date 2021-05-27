from iss_api_manager import IssApiManager
from sunset_sunrise_api_manager import SunsetSunriseApiManager

sunset_sunrise_parameters = {
    "lat": 19.432608,
    "lgn": -99.133209,
    "formatted": 0
}

iss_api = IssApiManager(end_point="http://api.open-notify.org/iss-now.json")
sunset_sunrise_api = SunsetSunriseApiManager(end_point="https://api.sunrise-sunset.org/json",
                                             parameters=sunset_sunrise_parameters)

print(iss_api.get_iss_coordinates())
print(sunset_sunrise_api.get_sunset_sunrise_hours())