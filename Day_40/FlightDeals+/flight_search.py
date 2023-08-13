import requests
import datetime

# Constants
API_KEY = "lfKv2PNdNQh1CsSs2TyIJT2ZJuqv_ZWm"
HEADER = {
    'apikey': API_KEY
}
FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
FLIGHT_FROM = "LON"
FLIGHT_TYPE = "direct"
LEAVE = "tomorrow to 6 months"
STAY = "7 to 28 days"
CURRENCY = "GBP"

FLIGHT_PARAMS = {
    'fly_from': 'LON',
    'fly_to': '',
    'date_from': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
    'date_to': (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%d/%m/%Y"),
    'nights_in_dst_from': 7,
    'nights_in_dst_to': 28,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "GBP"
}


class FlightSearch:

    def name(self, city):
        self.city = city

        flight_params = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=FLIGHT_ENDPOINT, params=flight_params, headers=HEADER)
        return response.json()['locations'][0]['code']

    def cheap_flight(self, x):
        flight_price = []
        FLIGHT_PARAMS['fly_to'] = x
        try:
            response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=FLIGHT_PARAMS, headers=HEADER)
            departure = response.json()['data'][0]['local_departure'].split('T')[0]
            arrival = response.json()['data'][0]['local_arrival'].split('T')[0]
            price = response.json()['data'][0]['price']
            city = response.json()['data'][0]['cityTo']
            city_code = response.json()['data'][0]['cityCodeTo']
            flight_price.append({
                'price': price,
                'city': city,
                'city_code': city_code,
                'departure': departure,
                'arrival': arrival
            })
        except IndexError:
            flight_price = None

        return flight_price
