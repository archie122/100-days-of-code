import requests
from datetime import datetime, timedelta
import smtplib

# Email User and Password
EMAIL = "t72189519@gmail.com"
PASSWORD = "tdqwngwakikmzexk"

# Company and Stock
STOCK = "AAPL"
COMPANY_NAME = "Apple"

# API keys
NEWS_API_KEY = 'e42f49b16aca41668c331d1e44434d2b'
STOCKS_API_KEY = '0I9P3BWUWIY2SDLN'

# Stock API
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCKS_API_KEY}"
r = requests.get(url)
data = r.json()

# Date and Time
last_refreshed = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
before_yesterday = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")

# Closing Price

closing_price1 = data["Time Series (Daily)"][last_refreshed]["4. close"]
closing_price2 = data["Time Series (Daily)"][before_yesterday]["4. close"]

closing_percentage_change = round(((float(closing_price1) - float(closing_price2)) / float(closing_price1)), 2) * 100

# News API
news_url = (f"https://newsapi.org/v2/everything?"
            f"q={COMPANY_NAME}"
            f"&from={last_refreshed}"
            f"&sortBy=publishedAt"
            f"&sortBy=popularity"
            f"&apiKey={NEWS_API_KEY}")

news_response = requests.get(news_url)
news_data = news_response.json()

# Email Data
up_or_down = f"{closing_percentage_change}% down" if closing_percentage_change < 0 else f"{closing_percentage_change}% up"


# Email
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # Encrypting the connection
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="archie.c122133@gmail.com",
        msg=f"Subject: {STOCK} {up_or_down}\n\n"
             f"Headline 1 : {news_data['articles'][0]['title']}\n {news_data['articles'][0]['description']}\n\n"
             f"Headline 2 : {news_data['articles'][1]['title']}\n {news_data['articles'][1]['description']}\n\n"
             f"Headline 3 : {news_data['articles'][2]['title']}\n {news_data['articles'][2]['description']}".encode('utf-8'))