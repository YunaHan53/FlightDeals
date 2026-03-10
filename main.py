from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flights = FlightSearch()

sheet_data = data_manager.get_data()
for row in sheet_data:
    row_id = row["id"]
    city = row["city"]
    code = row["iataCode"]
    data = {
        "city": city
    }
    iata_code = flights.get_flight_search(data)
    row["iataCode"] = iata_code
    data_manager.post_data(row_id, iata_code)

print(sheet_data)