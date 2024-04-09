from bs4 import BeautifulSoup
import requests
import lxml


class PriceSearch:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)

        self.soup = BeautifulSoup(self.response.text, "lxml")

    def get_price(self):

        try:
            new_price = float(self.soup.find(class_="a-offscreen").get_text().replace(".", "_")
                              .replace(",", ".").strip("R$"))
        except ValueError:
            print("Price not found")
            return None

        return new_price
