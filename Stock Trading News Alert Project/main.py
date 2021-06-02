import datetime
import os
import requests
from twilio.rest import Client

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
RECIPIENT_PHONE_NUMBER = os.environ.get("RECIPIENT_PHONE_NUMBER")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
STOCK = "TSLA"
COMPANY_NAME = "TESLA"

alpha_vantage_arguments = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

news_api_arguments = {
    "q": COMPANY_NAME,
    "from": f"{datetime.datetime.now().date()}",
    "language": "en",
    "apiKey": NEWS_API_KEY
}

# ALPHA VANTAGE API
alpha_vantage_response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=alpha_vantage_arguments)
alpha_vantage_response.raise_for_status()
stock_data = [data for day, data in alpha_vantage_response.json()["Time Series (Daily)"].items()]
# Close price from yesterday
closing_price_one = float(stock_data[0]["4. close"])
# Close price from the day before yesterday
closing_price_two = float(stock_data[1]["4. close"])
price_percentage_change = round((closing_price_one - closing_price_two) * 100 / closing_price_one, 2)
print(f"Percentage difference in price: {price_percentage_change}")

# NEWS API
news_api_response = requests.get(url=NEWS_API_ENDPOINT, params=news_api_arguments)
news_api_response.raise_for_status()

if len(news_api_response.json()["articles"]) != 0:
    try:
        articles_list = news_api_response.json()["articles"][0:3]
    except IndexError as index_error_message:
        print(f"Error message: {index_error_message}")
        articles_list = news_api_response.json()["articles"][0:]
    finally:
        articles_selected = [{"title": article["title"],
                              "publishedAt": article["publishedAt"],
                              "description": article["description"],
                              "url": article["url"]} for article in articles_list]
    message = ""

    for article in articles_selected:
        message = message + f'Headline: {article["title"]} \n ' \
                            f'Date: {article["publishedAt"]} \n ' \
                            f'URL: {article["url"]} \n ' \
                            f'DESCRIPTION: {article["description"]} \n\n'
else:
    message = "There are no articles to show"

message = f"Stock: {STOCK} \n " \
          f"Percentage difference in price: {price_percentage_change} % \n" \
          f"{message}"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=RECIPIENT_PHONE_NUMBER)
print(message.status)


