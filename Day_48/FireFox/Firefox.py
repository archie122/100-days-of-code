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
browser.get('http://example.com')
