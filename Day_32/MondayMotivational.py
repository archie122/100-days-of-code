import datetime
import smtplib
import random

EMAIL = "t72189519@gmail.com"
PASSWORD = "tdqwngwakikmzexk"
DAY = datetime.datetime.now().day

day_dict = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

if DAY == 6:
    with open("quotes.txt", "r") as file:
        filedata = file.readlines()
        quote = random.choice(filedata)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() #Encrypting the connection
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="archie.c122133@gmail.com",
            msg=f"Subject:Happy {day_dict[DAY]}!!\n\nHere is the quote for today : {quote}")

