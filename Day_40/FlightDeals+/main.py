import requests
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

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
notification = NotificationManager()


# Sheety API
response = requests.get(url=SHEET_ENDPOINT, headers=HEADER)
sheet_data = response.json()

# Updating the spreadsheet
for x in sheet_data:
    if x['iataCode'] == '':
        x['iataCode'] = flight_search.name(x['city'])
        data.update_flight_data(x['iataCode'], x['id'])

    price = flight_search.cheap_flight(x['iataCode'])

    if price is None:
        continue

    print(price[0]['price'])
    # if int(price['price']) < int(x['lowestPrice']):
    #     flight_data = {
    #         'price': price['price'],
    #         'departure_city_name': 'London',
    #         'departure_city_code': 'LON',
    #         'arrival_city_name': price['city'],
    #         'arrival_city_code': price['city_code'],
    #         'departure_date': price['departure'],
    #         'arrival_date': price['arrival']
    #     }
    #     notification.send_email(flight_data)


