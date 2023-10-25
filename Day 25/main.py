# reading the csv file

with open("weather_data.csv") as wdata:
    data = wdata.readlines()
    print(data)

# reading csv with csv module

import csv

with open("weather_data.csv") as wdata:
    data = csv.reader(wdata)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(row[1])
    print(temperature)

# reading the csv file with pandas

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)

# get the temperature
print(data["temp"])

# convert dataframe to dict
dict_data = data.to_dict()
print(dict_data)

# convert series to list
list_data = data["temp"].to_list()
print(list_data)

# get the mean and maximum values
print(data["temp"].mean())
print(data["temp"].max())

# different ways to get the data from column
print(data["condition"])
print(data.condition)

# get the data from row based on condition
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# create dataframe from scratch
student_scores = {
    "names": ["James", "John", "Speed"],
    "scores": [89, 85, 95]
}

data = pd.DataFrame(student_scores)
print(data)

# save the data as csv
data.to_csv("student_scores.csv")