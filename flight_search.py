import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.serp_api_endpoint = os.getenv("SERP_API_ENDPOINT")
        self.serp_api_key = os.getenv("SERP_API_KEY")

    def get_iata_code(self, city_name: str) -> str:
        params = {
            "engine": "google_flights_autocomplete",
            "api_key": self.serp_api_key,
            "q": city_name,
        }
        response = requests.get(self.serp_api_endpoint, params=params)
        response.raise_for_status()

        airports = response.json()["suggestions"][0]["airports"]
        iata_codes_list = [airport["id"] for airport in airports]
        iata_codes = ",".join(iata_codes_list)
        return iata_codes
