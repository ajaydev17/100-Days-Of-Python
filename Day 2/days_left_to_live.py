# print some welcome message
print("Welcome............................!!!\n")

# ask the user for input
current_age = int(input("How old are you ? : "))

age_left = 90 - current_age

days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12

print(f"Congrats!!, You have got {days_left} days, {weeks_left} weeks and {months_left} months to live!!!")