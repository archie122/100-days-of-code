import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the chromedriver executable
chromedriver_path = "/Users/architchoudhary/Desktop/Programming/Drivers/chromedriver"

# Set up the service (optional, but useful for advanced configuration)
chrome_service = Service(chromedriver_path)

# Create the Chrome WebDriver instance using the service and options
browser = webdriver.Chrome(service=chrome_service)

# Perform actions in the browser
browser.get('https://en.wikipedia.org/wiki/Main_Page/')

# ... perform other actions ...

# Find the element by class name
articles = browser.find_element(by="id", value="articlecount")
articles_count = articles.find_element(by="css selector", value="a").text
print(articles_count)

# Add a delay to keep the browser window open for 10 seconds
time.sleep(10)

# Close the browser window and end the WebDriver session
browser.quit()
