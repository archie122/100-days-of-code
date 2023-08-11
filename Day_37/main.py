# HTTP GET Request : It is a request to retrieve information from a server.
# HTTP POST Request : It is a request to send information to a server.
# HTTP PUT Request : It is a request to modify information on a server.
# HTTP DELETE Request : It is a request to delete information on a server.

import requests
import datetime

USERNAME = 'archie122'
TOKEN = '09ev5w80bt45v9b4v56wn09340987435780f543h543780'
GRAPH_ID = 'graph1'
HEADERS = {
    'X-USER-TOKEN': TOKEN
}


# Setting up the user

pixela_endpoint = 'https://pixe.la/v1/users'

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
# The code above is used to check whether the post request is successful or not.

# Setting up the graph

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_parameters = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'hr',
    'type': 'float',
    'color': 'ajisai',
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

# Setting up the pixel

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixel_parameters = {
    'date': datetime.datetime.now().strftime('%Y%m%d'),
    'quantity': '1.5',
}

# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=HEADERS)
# print(response.text)


# Updating the pixel

pixel_update_endpoint = f'{pixel_endpoint}/{datetime.datetime.now().strftime("%Y%m%d")}'
pixel_update_parameters = {
    'quantity': '5',
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_parameters, headers=HEADERS)
# print(response.text)

# Deleting the pixel

response = requests.delete(url=pixel_update_endpoint, json=pixel_update_parameters, headers=HEADERS)
print(response.text)
