import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Twitter_Bot:
    def __init__(self, username, password, path):
        self.TWITTER_USERNAME = username
        self.TWITTER_PASSWORD = password
        self.path = path

        chrome_service = Service(self.path)
        self.browser = webdriver.Chrome(service=chrome_service)

        self.login()

    def login(self):
        self.browser.get('https://twitter.com/i/flow/login')

        time.sleep(2)

        username = self.browser.find_element(by=By.XPATH,
                                             value='/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div['
                                                   '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                   '2]/div/input')
        username.send_keys(self.TWITTER_USERNAME)

        button1 = self.browser.find_element(by=By.XPATH,
                                            value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        button1.click()

        time.sleep(2)

        password = self.browser.find_element(by=By.XPATH,
                                             value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                                   '2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div['
                                                   '2]/div[1]/input')
        password.send_keys(self.TWITTER_PASSWORD)

        button2 = self.browser.find_element(by=By.XPATH,
                                            value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        button2.click()

        time.sleep(2)

    def create_post(self, text):
        post_button = self.browser.find_element(by=By.XPATH,
                                                value='/html/body/div[1]/div/div/div[2]/header/div/div/div/div['
                                                      '1]/div[3]/a/div')
        post_button.click()

        time.sleep(2)

        tweet = self.browser.find_element(by=By.XPATH,
                                          value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div['
                                                '2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div['
                                                '2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div['
                                                '1]/div/div/div/div/div/div[2]/div')
        tweet.send_keys(text)

        time.sleep(2)

    def post_tweet(self):
        post_tweet = self.browser.find_element(by=By.XPATH,
                                               value='/html/body/div[1]/div/div/div[1]/div['
                                                     '2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div['
                                                     '2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div')
        post_tweet.click()

        time.sleep(2)

    def quit(self):
        self.browser.quit()
