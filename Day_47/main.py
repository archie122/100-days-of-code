import smtplib
import requests
from bs4 import BeautifulSoup

URL = (
    'https://www.amazon.ca/dp/B09YR47XHV/?coliid=I19CUMJ4WSCUML&colid=271SMJD5JLZ4G&psc=1&ref_=list_c_wl_gv_ov_lig_pi_dp')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3'
}
EMAIL = "t72189519@gmail.com"
PASSWORD = "tdqwngwakikmzexk"

response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')
price = int(soup.select('.priceToPay .a-price-whole')[0].getText().split('.')[0])

if price < 150:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Encrypting the connection
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="archie.c122133@gmail.com",
            msg=f"Subject: Amazon Price Alert\n\n"
                f'The LETSHUOER S12 has dropped to ${price}!\n'
                f'Link to the product : {URL}')
else:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Encrypting the connection
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="archie.c122133@gmail.com",
            msg=f"Subject: Amazon Price Alert\n\n"
                f'The LETSHUOER S12 is still ${price}!\n'
                f'Link to the product : {URL}')
