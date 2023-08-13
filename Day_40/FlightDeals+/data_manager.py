import requests


class DataManager:
    def __init__(self, sheet_endpoint, header):
        self.sheet_endpoint = sheet_endpoint
        self.header = header

    def update_flight_data(self, data, id):
        sheet_inputs = {
            'price': {
                'iataCode': data
            }
        }
        response = requests.put(url=self.sheet_endpoint + f"/{id}", json=sheet_inputs, headers=self.header)
