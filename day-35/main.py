from dotenv import load_dotenv
import os
import requests

load_dotenv()

END_PONT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("API_KEY")
MY_LON = float(os.getenv("MY_LON"))
MY_LAT = float(os.getenv("MY_LAT"))

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "count": 4,
    "appid": API_KEY,
}

response = requests.get(url=END_PONT, params=params)
print(response.json())




