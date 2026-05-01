import requests
from pprint import pprint
import os
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv('usernam')
PASSWORD = os.environ['PASSWORD']
TOKEN = os.environ['TOKEN']

headers = {
    "Authorization": TOKEN

}

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_PRICES_ENDPOINT')
SHEETY_USERS_ENDPOINT = os.getenv('SHEETY_USERS_ENDPOINT')


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=(USERNAME, PASSWORD), headers=headers)
        # print()
        # print(self.response)
        # self.print_sheet_data()
        self.destination_data = {}
        self.customer_data = {}

    def sheet_data(self):
        return self.response.json()['prices']

    def print_sheet_data(self):
        pprint(self.response.json()['prices'])

    def update_sheet(self):
        body = {
            "price": {
                'iataCode': 'UPDATING'
            }
        }

        for row in range(len(self.sheet_data())):
            response = requests.put(url=f'{SHEETY_PRICES_ENDPOINT}/{row+2}', json=body, auth=(USERNAME, PASSWORD), headers=headers)
            print(response.json())

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=(USERNAME, PASSWORD),
                headers=headers
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth=(USERNAME, PASSWORD), headers=headers)
        data =  response.json()['users']
        self.customer_data = data
        return self.customer_data


