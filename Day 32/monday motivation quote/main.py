import smtplib
from datetime import datetime
import random

now = datetime.now()
current_weekday = now.weekday()

user = ""
password = ""
to_address = ""

if current_weekday == 0:
    with open("quote.txt", encoding="utf8") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(
            from_addr=user,
            to_addrs=to_address,
            msg=f"Subject:Monday Motivation\n\n{random_quote}".encode("utf8")
        )
