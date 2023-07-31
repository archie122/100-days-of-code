import pandas

data = pandas.read_csv("squirrel_data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])


squirrel_data = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

new_data = pandas.DataFrame(squirrel_data)
new_data.to_csv("squirrel_colour_data.csv")
print(new_data)