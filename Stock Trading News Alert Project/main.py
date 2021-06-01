import os
import requests

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

alpha_vantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": ALPHA_VANTAGE_API_KEY
}

alpha_vantage_response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=alpha_vantage_parameters)
alpha_vantage_response.raise_for_status()
stock_data = [data for day, data in alpha_vantage_response.json()["Time Series (Daily)"].items()]
yesterday_close_price = float(stock_data[0]["4. close"])
the_night_before_last_close_price = float(stock_data[1]["4. close"])
print(yesterday_close_price)
print(the_night_before_last_close_price)
