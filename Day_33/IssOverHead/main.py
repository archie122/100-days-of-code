import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.048615  # Your latitude
MY_LONG = -114.070847  # Your longitude
EMAIL = "t72189519@gmail.com"  # Your email
PASSWORD = "tdqwngwakikmzexk"  # Your password

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_it_dark(sunrise, sunset, time_now):
    if time_now >= sunset + 12 and time_now <= sunrise:
        return True
    else:
        return False


# Parameters for a route
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Getting the data from the API
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

while True:
    if iss_overhead() and is_it_dark(sunrise, sunset, time_now):
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls() #Encrypting the connection
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="testing12345555@yahoo.com",
                msg="Subject:The ISS is above!\n\n Hey, look up! The ISS is above you!")
    time.sleep(6000)


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
