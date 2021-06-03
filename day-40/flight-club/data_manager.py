from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d5297cf9d391279d3e9731d72f2f6f75/flightDeals"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        try:
            response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}/prices")
            response.raise_for_status()
            data = response.json()
            self.destination_data = data["prices"]
            return self.destination_data
        except requests.exceptions.HTTPError as error_msg:
            print(error_msg)

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/prices/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_users(self):
        try:
            response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}/users")
            response.raise_for_status()
            data = response.json()
            self.user_data = data["users"]
            return self.user_data
        except requests.exceptions.HTTPError as error_msg:
            print(error_msg)

    def post_new_users(self, first_name: str, last_name: str, email: str) -> str:
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        try:
            response = requests.post(url=f"{SHEETY_PRICES_ENDPOINT}/users", json=new_data)
            response.raise_for_status()
            return "success"
        except requests.exceptions.HTTPError as error_msg:
            return str(error_msg)
