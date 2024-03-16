from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()

END_PONT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("API_KEY")
MY_LON = float(os.getenv("MY_LON"))
MY_LAT = float(os.getenv("MY_LAT"))
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
MY_PHONE = os.getenv("MY_PHONE")

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(url=END_PONT, params=params)
data = response.json()

will_rain = False
for w in data['list']:
    condition_code = w['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH)

    message = client.messages \
                    .create(
                         body="It's going to rain today. Remember to bring an umbrella",
                         from_=TWILIO_PHONE,
                         to=MY_PHONE
                     )

    print(message.status)
