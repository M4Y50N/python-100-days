import pandas


class DataManage:
    def __init__(self):
        self.data = pandas.read_csv("products.csv")

