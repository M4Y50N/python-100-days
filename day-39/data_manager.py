from dotenv import load_dotenv
import requests
import os

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_flights(self):
        header = {
            "Authorization": f"Basic {AUTH_TOKEN}"
        }

        sheety_response = requests.get(SHEET_ENDPOINT, headers=header)
        data = sheety_response.json()["prices"]

        self.sheet_data = data

    def update_iata(self):
        header = {
            "Authorization": f"Basic {AUTH_TOKEN}"
        }
        for price in self.sheet_data:
            if price["iataCode"] == "":
                put_response = requests.put(SHEET_ENDPOINT + f"/{price["id"]}",
                                            json={
                                                "price":
                                                    {"iataCode": price["iataCode"]}
                                            }, headers=header,
                                            )

                print(put_response.text)
