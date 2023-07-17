# print some welcome message on the screen
print("Welcome to the leap year check app........................................\n")

# ask user for the input
year = int(input("Which year you want to check : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year!!")
else:
    print(f"{year} is not a leap year!!")