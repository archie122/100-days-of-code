import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Specify the path to the geckodriver executable
geckodriver_path = "/Users/architchoudhary/Desktop/Programming/Drivers/geckodriver"

# Set up the service (optional, but useful for advanced configuration)
firefox_service = Service(geckodriver_path)

# Set up Firefox options (optional)
firefox_options = webdriver.FirefoxOptions()
# Add any desired options to firefox_options

# Create the Firefox WebDriver instance using the service and options
browser = webdriver.Firefox(service=firefox_service, options=firefox_options)

# Now you can use the 'browser' object to interact with the Firefox browser
browser.get('https://www.python.org/')

# Add a delay to keep the browser window open for 5 seconds
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
# Close the browser window and end the WebDriver session
browser.quit()

