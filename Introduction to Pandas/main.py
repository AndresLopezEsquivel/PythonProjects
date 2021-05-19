# import csv
# WEATHER_FILE_NAME = "weather_data.csv"
# with open(WEATHER_FILE_NAME) as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

WEATHER_FILE_NAME = "weather_data.csv"

# DataFrame
weather_data = pd.read_csv(WEATHER_FILE_NAME)
# Series
temperature_data = weather_data["temp"]
# Converting DataFrame to a dictionary
weather_data_dictionary = weather_data.to_dict()
# Converting Series to a list
temperature_data_list = temperature_data.to_list()
# Calculating the average of temperatures
average_of_temperatures = weather_data.temp.mean()
print(f"1) Average of temperatures: {average_of_temperatures}")
max_value_of_temperatures = weather_data.temp.max()
print(f"2) Maximum value of temperatures: {max_value_of_temperatures}")
# Get data in row
monday_weather_data = weather_data[weather_data.day == "Monday"]
print("3) Monday weather data: ")
print(monday_weather_data)
monday_temperature_fahrenheit = (9/5) * int(monday_weather_data.temp) + 32
print(f"4) Monday temperature in Fahrenheit: {monday_temperature_fahrenheit} [F]")
weather_data_of_day_with_highest_temperature = weather_data[weather_data.temp == max_value_of_temperatures]
print("5) Weather data of the day with the highest temperature: ")
print(weather_data_of_day_with_highest_temperature)