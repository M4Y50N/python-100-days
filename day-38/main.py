from dotenv import load_dotenv
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

print(response.json())
