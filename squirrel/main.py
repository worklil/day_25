import pandas

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": []
}
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# TODO: How many Gray, Cinnamon and BLack
# Primary Fur Color
# TODO: Build new type of data "squirrel_count.csv"
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(data[data["Primary Fur Color"] == data["Primary Fur Color"].max()])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

