from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flights = FlightSearch()

sheet_data = data_manager.get_data()
for row in sheet_data:
    row_id = row["id"]
    city = row["city"]
    code = row["iataCode"]

    # Only fetch if iataCode is empty
    if code == "":
        iata_codes = flights.get_iata_code(city)
        print(f"{city} -> {iata_codes}")

        row["iataCode"] = iata_codes
        data_manager.post_data(row_id, iata_codes)

# print(sheet_data)