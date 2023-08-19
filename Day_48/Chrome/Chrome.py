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
browser.get('http://example.com')
# ... perform other actions ...

# Add a delay to keep the browser window open for 5 seconds
time.sleep(5)

# Close the browser window and end the WebDriver session
browser.quit()
