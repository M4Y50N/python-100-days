from dotenv import load_dotenv
import requests
import os
from twilio.rest import Client

load_dotenv()

BULL = "🔺2%"
BEAR = "🔻5%"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
MY_PHONE = os.getenv("MY_PHONE")


def get_stock_info():
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={"PETR4.SAO"}&apikey={STOCK_API_KEY}")
    data = response.json()["Time Series (Daily)"]
    data_keys = list(data.keys())

    today = float(data[data_keys[0]]['2. high'])
    yesterday = float(data[data_keys[1]]['2. high'])

    if today >= yesterday * 1.02:
        send_sms("bull")
    elif today * 1.05 <= yesterday:
        send_sms("bear")


def get_stock_news():
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={"petr4"}&from=2024-03-13&sortBy=popularity&apiKey={NEWS_API_KEY}")
    data = response.json()["articles"][:3]

    articles = []
    for article in data:
        articles.append({'title': article['title'], 'description': article['description']})

    return articles


def send_sms(up_down):
    articles = get_stock_news()

    sms_articles = ""
    for article in articles:
        sms_articles += (f"Headline: {article['title']}\n"
                         f"Brief: {article['description']}\n\n")

    sms_message = f"{"PETR4"} {BULL if up_down == "bull" else BEAR}\n" + sms_articles

    client = Client(TWILIO_SID, TWILIO_AUTH)

    message = client.messages \
        .create(
        body=sms_message,
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )

    print(message.status)


get_stock_info()
