import smtplib
import pandas
from datetime import datetime
import random

# get the current month and day
today_tuple = (datetime.now().month, datetime.now().day)

# read the csv data of birthday list
data = pandas.read_csv("birthdays.csv")

# create the birthday dictionary
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# smtp details
user = ""
password = ""

if today_tuple in birthdays_dict:
    birthday_persons_details = birthdays_dict[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_persons_details["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(
            from_addr=user,
            to_addrs=birthday_persons_details["email"],
            msg=f"Subject:Happy Birthday!!\n\n{content}"
        )
