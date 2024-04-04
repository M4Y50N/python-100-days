from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import math

ORIGIN_CITY = "AJU"

data_manager = DataManager()
data_manager.get_flights()

# Update IATA codes
is_updatable = False
for index, data in enumerate(data_manager.sheet_data):
    # Check if IATA code is empty
    if isinstance(data["IATA Code"], float):
        is_updatable = True
        fight_search = FlightSearch()
        code = fight_search.get_iata_code(data["City"])
        data["IATA Code"] = code

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Get lower prices
lowest_flights = []
for destination in data_manager.sheet_data:
    fs = FlightSearch()
    flight = fs.get_flight(ORIGIN_CITY, destination["IATA Code"], tomorrow, six_month_from_today)

    if flight:
        if flight.price < destination["Lowest Price"] or math.isnan(destination["Lowest Price"]):
            is_updatable = True
            destination["Lowest Price"] = flight.price
            lowest_flights.append(flight)

if is_updatable:
    data_manager.update_iata()


notification_manager = NotificationManager()
notification_manager.send_message(lowest_flights)
