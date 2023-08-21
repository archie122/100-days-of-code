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
browser.get('https://www.linkedin.com/jobs/search/?currentJobId=3684447197&f_AL=true&geoId=102199904&keywords=Junior%20Python%20developer&location=Calgary%2C%20Alberta%2C%20Canada&refresh=true&sortBy=R')
# ... perform other actions ...

sign_in = browser.find_element(by='css selector', value='.nav__button-secondary')
sign_in.click()

username = browser.find_element(by='id', value='username')
username.send_keys('archit190rec@icloud.com')
password = browser.find_element(by='id', value='password')
password.send_keys('SS')

sumbit_button = browser.find_element(by='class name', value='from__button--floating')
sumbit_button.click()



# Add a delay to keep the browser window open for 5 seconds
time.sleep(200)

# Close the browser window and end the WebDriver session
browser.quit()
