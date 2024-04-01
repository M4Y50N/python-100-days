# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
data_manager.get_flights()

# Update IATA codes
for data in data_manager.sheet_data:
    # Check if IATA code is empty
    if data["iataCode"] == "":
        fight_search = FlightSearch()
        code = fight_search.get_iata_code(data["city"])
        data["iataCode"] = code

        data_manager.update_iata(city_id=data["id"], iata_code=data["iataCode"])

