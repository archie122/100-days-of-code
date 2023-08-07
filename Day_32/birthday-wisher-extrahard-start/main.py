import pandas
import random
import smtplib
import datetime

# Email and password
EMAIL = "t72189519@gmail.com"
PASSWORD = "tdqwngwakikmzexk"

# Accessing the data
data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient="records")

# Seeing today's date
month = datetime.datetime.now().month
date = datetime.datetime.now().date().day

# Choosing a random letter
letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter_templates_choice = random.choice(letter_templates)

# Finding the person
for person in birthdays_dict:
    if person['month'] == month and person['day'] == date:
        print('Happy Birthday', person['name'])

        # Create a letter
        with open("./letter_templates/" + letter_templates_choice, 'r') as f:
            letter = f.read()
            letter = letter.replace("[NAME]", person['name'])
        letter_templates_choice = random.choice(letter_templates)

        # Sending the letter
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Encrypting the connection
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=person['email'],
                msg=f'Subject:Happy Birthday!\n\n{letter}'
            )
