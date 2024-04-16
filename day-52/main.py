import os
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PAGE = os.getenv("PAGE")


class InstagramBot:
    def __init__(self, qtd):
        self.to_follow = []
        # Qtd of users to follow divide by 10
        self.qtd = int(qtd)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("https://www.instagram.com/")

        time.sleep(2)

        self.driver.find_element(By.NAME, value="username").send_keys(EMAIL)
        self.driver.find_element(By.NAME, value="password").send_keys(PASSWORD, Keys.ENTER)

        time.sleep(3)

        self.driver.get(f"https://www.instagram.com/{PAGE}/")

        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 value='//div[starts-with(@id, mount_0_0)]/div/div/div[2]/div/div/div[1]/div[1]/div['
                                       '2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span').click()

    def follow_users(self):
        for user in self.to_follow:
            if user.text == "Seguir":
                if not self.qtd:
                    break

                try:
                    user.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    print("Probably you can't follow more users now.")
                    self.qtd = 0



        scroll_origin = ScrollOrigin.from_element(self.to_follow[-1], 0, -50)
        ActionChains(self.driver) \
            .scroll_from_origin(scroll_origin, 0, 200) \
            .perform()

    # Finds 10 users per time
    def get_users(self):
        time.sleep(3)
        user_list = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        self.to_follow = user_list


follow_bot = InstagramBot(10.3)

for _ in range(follow_bot.qtd):
    follow_bot.get_users()
    follow_bot.follow_users()
    time.sleep(2)

print("#### Following is over!! #####")
