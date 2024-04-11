from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

big_cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
products_ids = [product.get_attribute("id") for product in store]

timeout = time.time() + 1
five_min = time.time() + 60 * 5

while True:
    big_cookie.click()

    if time.time() > timeout:
        money = int(driver.find_element(By.ID, value="money").text.replace(",", "_"))

        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        affordable_prices = []
        for i, price in enumerate(item_prices):
            if money > price:
                affordable_prices.append({"price": price, "id": products_ids[i]})

        if len(affordable_prices):
            driver.find_element(by=By.ID, value=affordable_prices[-1]["id"]).click()

        timeout += 5
