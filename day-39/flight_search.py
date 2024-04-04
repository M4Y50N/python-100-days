from dotenv import load_dotenv
import requests
import os

from flight_data import FlightData

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

    def get_flight(self, fly_from, fly_to, date_from, date_to):
        query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            # "max_stopovers": 0,
            "curr": "BRL"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=self.header, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"There's no flight to this destination {fly_to}")
            return None

        dest_city = None
        for r in data["route"]:
            if r["flyTo"] == fly_to:
                dest_city = r["cityTo"]
                break

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=dest_city,
            destination_airport=fly_to,
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][len(data["route"])-1]["local_departure"].split("T")[0],
            link=data["deep_link"]
        )
        print(f"{flight_data.destination_city}: R${flight_data.price}")

        return flight_data
