import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
        self.SHEET_AUTH_TOKEN = os.getenv("SHEET_AUTH_TOKEN")
        self.sheet_headers = {
                "Authorization": f"Bearer {self.SHEET_AUTH_TOKEN}"
        }

    def get_data(self):
        response = requests.get(self.SHEET_ENDPOINT, headers=self.sheet_headers)
        sheet_data = response.json()["prices"]
        return sheet_data

    def post_data(self, row_id: int, iata_code: str):
        update_endpoint = f"{self.SHEET_ENDPOINT}/{row_id}"
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(update_endpoint,json=body,headers=self.sheet_headers)
        print(f"Updated row {row_id} → {iata_code} | Status: {response.status_code}")
