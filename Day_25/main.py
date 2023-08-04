# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# The panda module has two basic data structures: Series and DataFrame.

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# Whenever you choose to use a CSV file with pandas, the data type is pandas.core.frame.DataFrame

# print(data["temp"])
# Whenever you access a column, the data type is pandas.core.series.Series

# Challenge 1
# data_dict = data.to_dict()
# print(data_dict)
# print(data["temp"].to_list())

# Challenge 2
    # print(round(data["temp"].mean(), 2))
    # print(data["temp"].max())

# These two lines are equivalent
    # print(data["temp"])
    # print(data.temp)

# Get Data in the Rows
    # print(data[data.day == "Monday"])
    # print(data[data.temp == data.temp.max()])

# Get Data in the Columns
#     monday = data[data.day == "Monday"]
#     celcius = int(monday.temp[0])
#     fahrenheit = celcius * 9/5 + 32
#     print(celcius)
#     print(fahrenheit)

# Creating a dataframe
#     data_dict = {
#         "students": ["Amy", "James", "Angela"],
#         "scores": [76, 56, 65]
#     }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)