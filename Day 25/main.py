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
