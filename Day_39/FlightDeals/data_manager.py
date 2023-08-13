import requests
import smtplib

EMAIL = "t72189519@gmail.com"
PASSWORD = "tdqwngwakikmzexk"


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

    def send_email(self, data):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Encrypting the connection
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="archie.c122133@gmail.com",
                msg=f'Subject:Flight Deals!!\n\nThere is a flight going from {data["departure_city_name"]}-{data["departure_city_code"]} to {data["arrival_city_name"]}-{data["arrival_city_code"]} on {data["departure_date"]} at {data["arrival_date"]}. The price is {data["price"]}.')

