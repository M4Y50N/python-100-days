from dotenv import load_dotenv
from datetime import datetime
import requests
import os

load_dotenv()

GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': os.getenv("APP_ID"),
    'x-app-key': os.getenv("API_KEY")
  }

natural_language = input("Type today's exercise: ")

parameters = {
    "query": natural_language,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
data = response.json()

# Add to sheets
sheet_endpoint = os.getenv("SHEET_ENDPOINT")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {
        "Authorization": f"Basic {os.getenv("AUTH_TOKEN")}"
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)
