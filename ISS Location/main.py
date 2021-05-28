from datetime import datetime
from email_manager import EmailManager
from iss_api_manager import IssApiManager
from sunset_sunrise_api_manager import SunsetSunriseApiManager

MY_LATITUDE = -50.279
MY_LONGITUDE = 74.7615
LATITUDE_ERROR = 5.0
LONGITUDE_ERROR = 5.0

sunset_sunrise_parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

iss_api = IssApiManager(end_point="http://api.open-notify.org/iss-now.json")
sunset_sunrise_api = SunsetSunriseApiManager(end_point="https://api.sunrise-sunset.org/json",
                                             parameters=sunset_sunrise_parameters)

iss_coordinates = iss_api.get_iss_coordinates()
iss_latitude = iss_coordinates[0]
iss_longitude = iss_coordinates[1]

iss_latitude_inside_interval = (MY_LATITUDE - LATITUDE_ERROR) < iss_latitude < (MY_LATITUDE + LATITUDE_ERROR)
iss_longitude_inside_interval = (MY_LONGITUDE - LONGITUDE_ERROR) < iss_longitude < (MY_LONGITUDE + LONGITUDE_ERROR)
iss_is_near = iss_latitude_inside_interval and iss_longitude_inside_interval

print(f"ISS coordinates: {iss_coordinates}")

if iss_is_near:
    current_hour = datetime.now().hour
    sunrise_sunset_hours = sunset_sunrise_api.get_sunrise_sunset_hours()
    sunrise_hour = sunrise_sunset_hours[0]
    sunset_hour = sunrise_sunset_hours[1]
    print(f"Hour: {current_hour}")
    print(f"Sunrise hour: {sunrise_hour}")
    print(f"Sunset hour: {sunset_hour}")
    iss_above_you = False
    if sunset_hour < current_hour or current_hour < sunrise_hour:
        iss_above_you = True

    if iss_above_you:
        subject = "The ISS is above you!"
        message = "You can see the ISS above you :')"
        recipient_email = ""
        email_manager = EmailManager(message=message, subject=subject, recipient_email=recipient_email)
        email_manager.send_email()