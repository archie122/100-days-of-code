#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

# Constants
SHEET_ENDPOINT = "https://api.sheety.co/8dd79b591323e6361ee4aa75abbe72f1/flightDeals/prices"
AUTHENTICATION = 'br6y4e6565bv45sfcerertfbnyymnmimuimntuij6663573673683636844utyijyui55'
HEADER = {
    'authorization': f'Bearer {AUTHENTICATION}'
}
COUNTRY_CODE = []

# Objects
flight_search = FlightSearch()
data = DataManager(SHEET_ENDPOINT, HEADER)


# Sheety API
response = requests.get(url=SHEET_ENDPOINT, headers=HEADER)
sheet_data = response.json()['prices']

# Updating the spreadsheet
for x in sheet_data:
    if x['iataCode'] == '':
        x['iataCode'] = flight_search.name(x['city'])
        data.update_flight_data(x['iataCode'], x['id'])
    else :
        COUNTRY_CODE.append(x['iataCode'])
# Finding the cheapest flight
prices = flight_search.cheap_flight(COUNTRY_CODE)

# Comparing the cheapest flight
for i in range(0, len(sheet_data)):
    if prices[i]['price'] < sheet_data[i]['lowestPrice']:
        flight_data = {
            'price': prices[i]['price'],
            'departure_city_name': 'London',
            'departure_city_code': 'LON',
            'arrival_city_name': prices[i]['city'],
            'arrival_city_code': prices[i]['city_code'],
            'departure_date': prices[i]['departure'],
            'arrival_date': prices[i]['arrival']
        }
        data.send_email(flight_data)


