import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.serp_api_endpoint = os.getenv("SERP_API_ENDPOINT")
        self.serp_api_key = os.getenv("SERP_API_KEY")

    def get_flight_search(self, data):
        return "TESTING"