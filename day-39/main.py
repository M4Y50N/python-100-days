# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

sheet_endpoint = os.getenv("SHEET_ENDPOINT")
sheety_header = {
    "Authorization": f"Basic {os.getenv("AUTH_TOKEN")}"
}

sheety_request = requests.get(sheet_endpoint, headers=sheety_header)
data = sheety_request.json()

for price in data["prices"]:
    put_request = requests.put(sheet_endpoint + f"/{price["id"]}",
                               json={
                                   "price":
                                       {"iataCode": "TESTING"}
                               }, headers=sheety_header,
                               )
    # print(put_request.json())

# pprint(data)
