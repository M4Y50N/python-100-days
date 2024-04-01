from dotenv import load_dotenv
import requests
import os

load_dotenv()

TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
TEQUILA_AFFILID = os.getenv("TEQUILA_AFFILID")
TEQUILA_APIKEY = os.getenv("TEQUILA_APIKEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city_name):
        header = {
            "apikey": TEQUILA_APIKEY,
        }

        query = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=query)

        return response.json()["locations"][0]["code"]
