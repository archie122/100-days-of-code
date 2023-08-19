import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the chromedriver executable
chromedriver_path = "/Users/architchoudhary/Desktop/Programming/Drivers/chromedriver"

# Set up the service (optional, but useful for advanced configuration)
chrome_service = Service(chromedriver_path)
browser = webdriver.Chrome(service=chrome_service)

# Perform actions in the browser
browser.get('https://www.amazon.ca/Oculus-Quest-Advanced-All-One/dp/B09B2YFYYX/?_encoding=UTF8&pd_rd_w=XrWqa&content-id=amzn1.sym.a33d7cb3-a403-494e-b920-61e26e386e19&pf_rd_p=a33d7cb3-a403-494e-b920-61e26e386e19&pf_rd_r=PXCR8CZMQ8D5SJH0TSRN&pd_rd_wg=MwTp8&pd_rd_r=7fe38c77-5fa0-4c39-9114-7b64200585ec&ref_=pd_gw_crs_zg_bs_3198031&th=1')

# ... perform other actions ...
price = browser.find_element(by="class name", value="a-price-whole")
print(price.text)

logo = browser.find_element(by="class name", value="nav-logo-link")
print(logo.size)

# Add a delay to keep the browser window open for 5 seconds
# time.sleep(5)

# Close the browser window and end the WebDriver session
browser.quit()