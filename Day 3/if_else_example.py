# print some welcome message on the console
print("Welcome to the roller coaster ride!!!\n")

# ask user for some input
height = int(input("Please enter your height in cm: "))

if height >= 120:
    print("Cograts!!, You are eligle for the ride!!!")

    # ask user for their age
    age = int(input("Please enter your age in years: "))

    if age >= 12 and age < 18:
        print("Please pay $5 at the counter and enjoy your ride!!!")
    elif age >= 18 and age < 24:
        print("Please pay $10 at the counter and enjoy your ride!!!")
    else:
        print("Please pay $15 at the counter and enjoy your ride!!!")

else:
    print("Sorry!!, You are too short for the ride!!!")