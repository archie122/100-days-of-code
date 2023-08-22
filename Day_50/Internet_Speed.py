import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Internet_Speed:
    def __init__(self, path):
        self.start_test = None
        self.download_speed = None
        self.upload_speed = None
        self.path = path

        chrome_service = Service(path)
        self.browser = webdriver.Chrome(service=chrome_service)

        self.start()

        self.download_speed = self.dspeed()
        self.upload_speed = self.uspeed()

    def start(self):
        self.browser.get('https://www.speedtest.net/')
        time.sleep(5)
        self.start_test = self.browser.find_element(by='xpath',
                                                    value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[1]/a')
        self.start_test.click()
        time.sleep(100)

    def dspeed(self):
        self.download_speed = self.browser.find_element(by='xpath',
                                                        value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div['
                                                              '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                              '1]/div/div[2]/span')
        return self.download_speed.text

    def uspeed(self):
        self.upload_speed = self.browser.find_element(by='xpath',
                                                      value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div['
                                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                            '2]/div/div[2]/span')
        return self.upload_speed.text

    def quit(self):
        self.browser.quit()
