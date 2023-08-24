import time

import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants

PATH = "/Users/architchoudhary/Desktop/Programming/Drivers/chromedriver"
SERVICE = Service(PATH)
BROWSER = webdriver.Chrome(service=SERVICE)
RENT_URL = "https://www.rentcafe.com/1-bedroom-apartments-for-rent/us/ca/san-francisco/?PriceMax=3000"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdVdrQ9sQAJiBBq0AU-jSYZ45PCitE6F1YxqXmTyEtHVyEOow/viewform"


def get_apartment_info():
    BROWSER.get(RENT_URL)

    address_list = BROWSER.find_element(by="xpath", value="/html/body/main/div[2]/div/div[1]/div/div/section/ul")
    street = address_list.find_elements(by="xpath", value="li/div[2]/div[2]/span")
    website = address_list.find_elements(by="xpath", value="li/div[2]/div[2]/h2/a")
    price = address_list.find_elements(by="xpath", value="li/div[2]/table/tbody/tr/td[2]")

    street_list = [street_name.text for street_name in street]
    website_list = [website_name.get_attribute("href") for website_name in website]
    price_list = [price_name.text for price_name in price]

    apartment_dict = {}

    for i in range(len(street_list)):
        apartment_dict[i] = [street_list[i], website_list[i], price_list[i]]

    time.sleep(5)
    BROWSER.quit()

    return apartment_dict


def put_into_pandas(apartment_dict):
    df = pandas.DataFrame(apartment_dict)
    df.to_dict(orient="index")
    df_transposed = df.transpose()
    df_transposed.to_dict(orient="index")
    print(df_transposed)
    df_transposed.to_csv("apartment_info.csv")


apartment_info = get_apartment_info()
put_into_pandas(apartment_info)