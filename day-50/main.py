import os
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

time.sleep(2)
driver.find_elements(By.CLASS_NAME, value="w1u9t036")[1].click()

time.sleep(1)
driver.find_element(By.XPATH, value='//*[@id="s-1041457679"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

email = os.getenv("EMAIL")
pass_w = os.getenv("PASSWORD")

time.sleep(2)

driver.switch_to.window(fb_login_window)
driver.find_element(By.XPATH, value='//*[@id="email"]').send_keys(email)
driver.find_element(By.XPATH, value='//*[@id="pass"]').send_keys(pass_w, Keys.ENTER)

time.sleep(5)

driver.find_element(By.XPATH, value="//div[starts-with(@id, mount_0_0)]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div").click()

time.sleep(2)

driver.switch_to.window(base_window)

time.sleep(5)

driver.find_element(By.XPATH, value='//*[@id="s-1041457679"]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div').click()

time.sleep(2)

driver.find_element(By.XPATH, value='//*[@id="s-1041457679"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()

time.sleep(2)

driver.find_element(By.XPATH, value='//*[@id="s-1041457679"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]').click()

time.sleep(5)

while True:
    driver.find_element(By.XPATH, value='//*[@id="Tinder"]/body').send_keys(Keys.ARROW_RIGHT)
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, value='//*[@id="s-1041457679"]/main/div/div[2]/button[2]/div[2]/div[2]/div').click()
    except ElementClickInterceptedException:
        time.sleep(3)
        driver.find_element(By.XPATH, value='//*[@id="s-1041457679"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()

