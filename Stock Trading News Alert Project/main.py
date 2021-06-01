import datetime
import os
import requests

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_vantage_arguments = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": ALPHA_VANTAGE_API_KEY
}

news_api_arguments = {
    "q": "TESLA",
    "from": f"{datetime.datetime.now().date()}",
    "language": "en",
    "apiKey": NEWS_API_KEY
}

alpha_vantage_response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=alpha_vantage_arguments)
alpha_vantage_response.raise_for_status()
stock_data = [data for day, data in alpha_vantage_response.json()["Time Series (Daily)"].items()]
# Close price from yesterday
closing_price_one = float(stock_data[0]["4. close"])
# Close price from the day before yesterday
closing_price_two = float(stock_data[1]["4. close"])
price_percentage_change = round((closing_price_one - closing_price_two) * 100 / closing_price_one, 2)
print(f"Percentage difference in price: {price_percentage_change}")

if abs(price_percentage_change) > 5:
    print("Get news")

news_api_response = requests.get(url=NEWS_API_ENDPOINT, params=news_api_arguments)
news_api_response.raise_for_status()
print(news_api_response.json())
