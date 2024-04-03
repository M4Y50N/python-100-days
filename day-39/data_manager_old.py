from dotenv import load_dotenv
import requests
import os

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


class DataManager:
    def __init__(self):
        self.sheet_data = {}
        self.header = {
            "Authorization": f"Basic {AUTH_TOKEN}"
        }

    def get_flights(self):
        sheety_response = requests.get(SHEET_ENDPOINT, headers=self.header)
        data = sheety_response.json()
        print(data)

        self.sheet_data = data

    def update_iata(self, city_id, iata_code):
        put_response = requests.put(SHEET_ENDPOINT + f"/{city_id}",
                                    json={
                                        "price":
                                            {"iataCode": iata_code}
                                    }, headers=self.header,
                                    )

        print(put_response.text)
