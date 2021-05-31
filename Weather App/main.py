import os
import requests
from twilio.rest import Client

TWILIO_PHONE_NUMBER = ""
RECIPIENT_PHONE_NUMBER = ""
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
WEATHER_API_APP_ID = os.environ.get("WEATHER_API_APP_ID")
WeatherAPI_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

arguments = {
    "lat": 19.432680,
    "lon": -99.134209,
    "appid": WEATHER_API_APP_ID,
    "exclude": "current,minutely,alerts"
}

response = requests.get(url=WeatherAPI_endpoint, params=arguments)

weather_data = response.json()
print(weather_data)

weather_id_first_12_hours = [hour["weather"][0]["id"] for hour in weather_data["hourly"][:12]]
raining_data = [hour_weather_id < 700 for hour_weather_id in weather_id_first_12_hours]
is_going_to_rain = True in raining_data
print(weather_id_first_12_hours)

if is_going_to_rain:
    message = "Take an umbrella, it is probably going to rain."
else:
    message = "Don't worry. It isn't going to rain."

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create( body=message, from_=TWILIO_PHONE_NUMBER, to=RECIPIENT_PHONE_NUMBER)
print(message.status)
