# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
data_manager.get_flights()

# fs = FlightSearch()
# fs.get_flight()

# Update IATA codes
is_empty = False
for index, data in enumerate(data_manager.sheet_data):
    # Check if IATA code is empty
    if isinstance(data["IATA Code"], float):
        is_empty = True
        fight_search = FlightSearch()
        code = fight_search.get_iata_code(data["City"])
        data["IATA Code"] = code

if is_empty:
    data_manager.update_iata()
