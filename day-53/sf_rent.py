from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import requests
import lxml
import time


class GetSFRent:
    def __init__(self):
        self.form_link = "https://forms.gle/EkAudCYzm5mDmuD1A"
        self.zillow_link = "https://appbrewery.github.io/Zillow-Clone/"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get(self.form_link)

        self.response = requests.get(self.zillow_link)
        self.soup = BeautifulSoup(self.response.text, "lxml")

    def get_rantal_list(self):
        rent_list = self.soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        print(len(rent_list))
        for ap in rent_list:
            address = ap.find(class_="StyledPropertyCardDataArea-anchor")
            address_text = address.get_text().strip("\n").strip()
            address_link = address.get("href")
            price = ap.find(class_="PropertyCardWrapper__StyledPriceLine").get_text().split("+")[0].split("/")[0] \
                .replace(",", "")
            self.send_form(address_text, price, address_link)

    def send_form(self, address, price, link):
        new_address = self.driver.find_element(By.XPATH,
                                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                     '2]/div/div[1]/div/div[1]/input')
        new_address.send_keys(address)
        new_price = self.driver.find_element(By.XPATH,
                                             value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                   '1]/div/div[1]/input')
        new_price.send_keys(price)
        new_link = self.driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                  '1]/div/div[1]/input')
        new_link.send_keys(link)
        send_form = self.driver.find_element(By.XPATH,
                                             value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        send_form.click()

        # Next answer
        self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
        time.sleep(0.7)
