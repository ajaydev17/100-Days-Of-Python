# print some welcome message on the console
print("Welcome to the roller coaster ride!!!\n")

# ask user for some input
height = int(input("Please enter your height in cm: "))

if height >= 120:
    print("Cograts!!, You are eligle for the ride!!!")

    # ask user for their age
    age = int(input("Please enter your age in years: "))

    if age >= 12 and age < 18:
        bill = 5
        print("Child tickets are $5")
    elif age >= 18 and age < 24:
        bill = 10
        print("Youth tickets are $110")
    elif age >= 45 and age <=55:
        bill = 0
        print("Everything is gonna be ok, habe a free ride on us!!")
    else:
        print("Adult tickets are $15")
        bill = 15

    want_photo = input("Do you want a photo to be taken? Y or N: ")
    if want_photo == 'Y':
        bill = bill + 3

    if bill > 0:
        print(f"Your bill is ${bill}, pay at the counter and enjoy your ride!!")
    else:
        print("Please collect the ticket at the counter and enjoy your ride!!")

else:
    print("Sorry!!, You are too short for the ride!!!")