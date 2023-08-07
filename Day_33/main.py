# API : a set of commands, functions and objects that to create projects and to interact with external systems. The
# date for API is usually stored in a JSON format.

# API Endpoints : the location of the API.

# API Requests : the process of sending HTTP requests to the API

# Response code : the status code of the response from the API
# 1XX : Wait
# 2XX : Success
# 3XX : Redirect
# 4XX : Client Error
# 5XX : Server Error


import requests
from datetime import datetime

    # response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # # response.raise_for_status() # If the status code is not 200, raise an exception
    # # response.json() # Convert the response to JSON
    #
    # data = response.json()["iss_position"]
    # #print(data) # Print the data from the response
    #
    # longitude = data["longitude"] # Get the longitude
    # latitude = data["latitude"]   # Get the latitude
    #
    # print(longitude, latitude)

# API Parameters : the way to pass the data to the API

parameters = {
    'lat': 51.048615,
    'lng': -114.070847,
    'formatted': 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

time = datetime.now()

print(time.hour)