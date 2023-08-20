import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

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
browser.get('https://en.wikipedia.org/wiki/Main_Page/')

# ... perform other actions ...

# Find the element by class name

# Clicking Links
# article_count = browser.find_element(by="css selector", value="#articlecount a")
# article_count.click()

# view_source = browser.find_elements(by="link text", value="View source")
# view_source[0].click()

# Entering Text
# search_bar = browser.find_element(by="name", value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)


# Add a delay to keep the browser window open for 10 seconds
time.sleep(10)

# Close the browser window and end the WebDriver session
browser.quit()
