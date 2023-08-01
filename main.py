# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# k = 0
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # TODO: average number
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # TODO:Get Data in Columns
print(data["condition"])
print(data.condition)

# TODO:Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp
# print(monday_temp)
# fahrenheit = (monday_temp * 1.8) + 32
# print(fahrenheit)

# TODO: Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
