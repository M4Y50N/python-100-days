import pandas


class DataManager:
    def __init__(self):
        self.data = pandas.read_csv("./data/flight_data.csv")
        self.sheet_data = None

    def get_flights(self):
        data_aux = []
        for index, row in self.data.iterrows():
            data_aux.append({"City": row["City"], "IATA Code": row["IATA Code"], "Lowest Price": row["Lowest Price"]})

        self.sheet_data = data_aux

    def update_iata(self):
        updated_csv = {"City": {}, "IATA Code": {}, "Lowest Price": {}}
        for i, data in enumerate(self.sheet_data):
            updated_csv["City"][i] = data["City"]
            updated_csv["IATA Code"][i] = data["IATA Code"]
            updated_csv["Lowest Price"][i] = data["Lowest Price"]

        self.data = pandas.DataFrame(updated_csv)
        self.data.to_csv("./data/flight_data.csv")
        print(self.data)

