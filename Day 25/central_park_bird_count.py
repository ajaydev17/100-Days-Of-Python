import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_column = "Primary Fur Color"

gray_squirrels_count = len(data[data[color_column] == "Gray"])
cinnamon_squirrels_count = len(data[data[color_column] == "Cinnamon"])
black_squirrels_count = len(data[data[color_column] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pd.DataFrame(data_dict)
df.to_csv("count.csv")


