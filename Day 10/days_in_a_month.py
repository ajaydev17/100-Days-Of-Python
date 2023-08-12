# function checks year in leap or not

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_of_month(year, month):
    if month > 12 or month < 1:
        return "Invalid input!!"

    days_in_month = ["31", "28", "31", "30", "31",
                     "30", "31", "31", "30", "31", "30", "31"]

    if is_leap_year(year) and month == 2:
        return "29"
    else:
        return days_in_month[month - 1]


year = int(input("please enter your year of choice: "))
month = int(input("please enter your month of choice: "))

number_of_days = days_of_month(year, month)
print(f"Your month of choice has {number_of_days} days in it!!")
