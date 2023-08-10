import requests

# API Authentication Key are keys that are used to authenticate requests to any API that is used in the project.
# In other words, these companies are selling data that they have collected. That is why some of the API keys
# are hidden from the public and cost money.

API_KEY = "cb2db0e9046271ba3dd39238bd09d713"
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": 46.734750,
    "lon": -65.429410,
    "appid": API_KEY
}

response = requests.get(url=API_ENDPOINT, params=parameters)
print(response.status_code)
if int(response.json()['weather'][0]['id']) <= 700:
    print("It's going to rain")
else:
    print("It's going to be sunny")
