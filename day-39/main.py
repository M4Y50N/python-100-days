from flight_search import FlightSearch
from data_manager import DataManager

from datetime import datetime, timedelta

ORIGIN_CITY = "SAO"

data_manager = DataManager()
data_manager.get_flights()

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

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

fs = FlightSearch()
for destination in data_manager.sheet_data:
    fs.get_flight(ORIGIN_CITY, destination["IATA Code"], tomorrow, six_month_from_today)