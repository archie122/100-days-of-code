from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys


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
browser.get('https://secure-retreat-92358.herokuapp.com/')

# First Name
first_name = browser.find_element(by="name", value="fName")
first_name.send_keys("Archie")

# Last Name
last_name = browser.find_element(by="name", value="lName")
last_name.send_keys("C")

# Email Address
email = browser.find_element(by="name", value="email")
email.send_keys("7Ls3Z@example.com")

# Submit
submit = browser.find_element(by="css selector", value="button[type='submit']")
submit.click()