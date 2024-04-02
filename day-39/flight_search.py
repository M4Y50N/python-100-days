from pprint import pprint

from dotenv import load_dotenv
import requests
import os

load_dotenv()

TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
TEQUILA_AFFILID = os.getenv("TEQUILA_AFFILID")
TEQUILA_APIKEY = os.getenv("TEQUILA_APIKEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {
            "apikey": TEQUILA_APIKEY,
        }

    def get_iata_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=self.header, params=query)

        return response.json()["locations"][0]["code"]

    def get_flight(self):
        query = {
            "fly_from": "SAO",
            "fly_to": "AJU",
            "date_from": "19/04/2024",
            "date_to": "21/04/2024",
            "max_stopovers": 0,
            "curr": "BRL"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=self.header, params=query)

        for flight in response.json()["data"]:
            print(flight["price"])
            print(flight["deep_link"])
