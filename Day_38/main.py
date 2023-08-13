import requests
import datetime
import os

# Sensitive Data
APP_ID = "21a013fd"
API_KEY = "92d4e3914fa18cfc60a0f6022a1506b3"
USER_ID = "8dd79b591323e6361ee4aa75abbe72f1"
AUTHENTICATION = '509348fdlkjglkjfdgfokj09203kedkdiei120923jrejejfr09sdfu23lkifds0823jklhrtk'
sheet_endpoint = 'https://api.sheety.co/8dd79b591323e6361ee4aa75abbe72f1/workoutTracker/workouts'
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

PROJECT_ID = "workoutTracker"
SHEET_ID = "workouts"

user_input = input("Tell me what exercise you did? : ")

HEADER = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'authorization': f'Bearer {AUTHENTICATION}'
}

exercise_parameters = {
    'query': user_input,
    'gender': 'male',
    'weight_kg': 75,
    'height_cm': 175,
    'age': 20
}

# I did 40 pushups, 30 ab crunches, 20 Burpee's, 20 diamond pushups, and 1 min plank.

# NLP API
response = requests.post(url=endpoint,json=exercise_parameters, headers=HEADER)
data = response.json()
print(data)

# Updating the spreadsheet


today_date = datetime.datetime.now().strftime("%d/%m/%Y")
today_time = datetime.datetime.now().strftime("%X")

for x in data['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': today_time,
            'exercise': x['name'].title(),
            'duration': x['duration_min'],
            'calories': x['nf_calories']
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=HEADER)
    print(sheet_response.text)