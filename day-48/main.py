from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.execute_script(f"window.localStorage.setItem('CookieClickerLang', '{"PT-BR"}');")
driver.refresh()

big_cookie = driver.find_element(By.ID, value="bigCookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    big_cookie.click()

    if time.time() > timeout:
        cookies = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0].replace(",", "_"))

        store = driver.find_element(By.CSS_SELECTOR, value="#store")

        products = store.find_elements(By.CSS_SELECTOR, value="#products div")[1:]

        store_items = []
        # Get Store Items
        for p in products:
            print(p)
            # price = p.find_element(By.CLASS_NAME, value="price").text.strip()
            # if price:
            #     store_items.append({
            #         "product": p,
            #         "price": int(price.replace(",", "_"))
            #     })

        driver.find_element(By.ID, value="product0").click()


        # Buy Upgrades
        # for p in store_items:
        #     if p["price"] >= cookies:
        #         p["product"].click()

        timeout += 5
