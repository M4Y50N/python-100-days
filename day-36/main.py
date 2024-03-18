from dotenv import load_dotenv
import requests
import os
from twilio.rest import Client

load_dotenv()

STOCK = "azul4"
BULL = "🔺"
BEAR = "🔻"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
MY_PHONE = os.getenv("MY_PHONE")


def get_stock_info():
    api_url = "https://www.alphavantage.co/query?"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": f"{STOCK}.SAO",
        "apikey": STOCK_API_KEY
    }
    response = requests.get(api_url, params)
    data = response.json()["Time Series (Daily)"]
    data_keys = list(data.keys())

    yesterday = float(data[data_keys[0]]['4. close'])
    before_yesterday = float(data[data_keys[1]]['4. close'])

    diff = yesterday - before_yesterday
    percentage_diff = round(abs(diff / yesterday) * 100, 2)

    if percentage_diff >= 5:
        send_sms(diff, percentage_diff)


def get_stock_news():
    api_url = "https://newsapi.org/v2/everything?"
    params = {
        "q": STOCK,
        # "from": "2024-03-13",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(api_url, params)
    data = response.json()["articles"][:3]

    articles = []
    for article in data:
        articles.append({'title': article['title'], 'description': article['description']})

    return articles


def send_sms(variation, percentage):
    articles = get_stock_news()

    sms_articles = ""
    for article in articles:
        sms_articles += (f"*Headline*: {article['title']}\n"
                         f"*Brief*: {article['description']}\n\n")

    sms_message = f"{STOCK} {f"{BULL}{percentage}%" if variation > 0 else f"{BEAR}{percentage}%"}\n" + sms_articles

    client = Client(TWILIO_SID, TWILIO_AUTH)

    message = client.messages \
        .create(
        body=sms_message,
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )

    print(message.status)


get_stock_info()


