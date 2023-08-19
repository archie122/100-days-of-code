import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the chromedriver executable
chromedriver_path = "/Users/architchoudhary/Desktop/Programming/Drivers/chromedriver"

# Set up the service (optional, but useful for advanced configuration)
chrome_service = Service(chromedriver_path)
browser = webdriver.Chrome(service=chrome_service)

# Perform actions in the browser
browser.get('https://www.python.org/')

# ... perform other actions ...
events_dictionary = {}

events = browser.find_element(by="css selector", value=".event-widget .menu")

event = events.find_elements(by="css selector", value="li")

count = 0
for i in event:
    time = i.find_element(by="css selector", value="time").text
    name = i.find_element(by="css selector", value="a").text
    events_dictionary[count] = {time, name}
    count += 1

print(events_dictionary)


# Add a delay to keep the browser window open for 5 seconds
# time.sleep(5)

# Close the browser window and end the WebDriver session
browser.quit()