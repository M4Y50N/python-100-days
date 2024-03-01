import pandas

# import csv
#
# with open("./weather_data.csv") as weather_csv:
#     data = csv.reader(weather_csv)
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
#

# data = pandas.read_csv("./weather_data.csv")
# monday = data[data.day == "Monday"]


squirrels = pandas.read_csv("squirrel_data.csv")

grey_color = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
cinnamon_color = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
black_color = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

dict_colors = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_color, cinnamon_color, black_color]
}

data = pandas.DataFrame(dict_colors)
data.to_csv("count_squirrel_colors.csv")
