import requests

end_point = "https://api.openweathermap.org/data/2.5/onecall"

arguments = {
    "lat": 19.432680,
    "lon": -99.134209,
    "appid": "",
    "exclude": "current,minutely,alerts"
}

response = requests.get(url=end_point, params=arguments)

weather_data = response.json()
print(weather_data)
# hourly_data = weather_data["hourly"]
# weather_id = [hour["weather"][0]["id"] for hour in hourly_data]
# weather_id_first_12_hours = [weather_id[index] for index in range(13)]
# raining_data = [id < 700 for id in weather_id_first_12_hours]
# is_going_to_rain = True in raining_data

weather_id_first_12_hours = [hour["weather"][0]["id"] for hour in weather_data["hourly"][:12]]
raining_data = [hour_weather_id < 700 for hour_weather_id in weather_id_first_12_hours]
is_going_to_rain = True in raining_data
print(weather_id_first_12_hours)

if is_going_to_rain:
    print("Take an umbrella, it is probably going to rain.")
else:
    print("Don't worry. It isn't going to rain.")
