import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the chromedriver executable
chromedriver_path = "/Users/architchoudhary/Desktop/Programming/Drivers/chromedriver"

# Set up the service (optional, but useful for advanced configuration)
chrome_service = Service(chromedriver_path)

# Set up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False  # Disable headless mode
# Add any desired options to chrome_options

# Create the Chrome WebDriver instance using the service and options
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Perform actions in the browser
browser.get('https://orteil.dashnet.org/experiments/cookie/')

# ... perform other actions ...

timeout = time.time() + 5
cookie = browser.find_element(by="id", value="cookie")
number_of_cookies = browser.find_element(by="id", value="money")
store = browser.find_elements(by="css selector", value="#store div")
store_items = [item.get_attribute("id") for item in store]
five_min = time.time() + 60 * 5


while True:
    cookie.click()
    time.sleep(0.05)
    if time.time() > timeout:
        timeout = time.time() + 5

        all_prices = browser.find_elements(by="css selector", value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for x in range(len(item_prices)):
            cookie_upgrades[store_items[x]] = item_prices[x]

        if "," in number_of_cookies.text:
            money = int(number_of_cookies.text.replace(",", ""))
        cookie_num = int(number_of_cookies.text)

        affordable_upgrades = {}
        for id, cost in cookie_upgrades.items():
            if cookie_num > cost:
                affordable_upgrades[cost] = id

        highest_price = max(affordable_upgrades)
        print(highest_price)
        to_buy = affordable_upgrades[highest_price]

        browser.find_element(by="id", value=to_buy).click()

        timeout = time.time() + 5

        if time.time() > five_min:
            cookie_per_s = browser.find_element(by="id", value="cps").text
            print(cookie_per_s)
            break
# Add a delay to keep the browser window open for 5 seconds
time.sleep(20)

# Close the browser window and end the WebDriver session
browser.quit()
