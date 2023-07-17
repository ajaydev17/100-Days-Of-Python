# print some welcome message on the screen
print("Welcome to the pizza delivery app...............................................\n")

# ask for some user input
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill_amount = 0

if size == "S":
    bill_amount = 5
elif size == "M":
    bill_amount = 20
else:
    bill_amount = 25

if add_pepperoni == "Y":
    if size == "S":
        bill_amount = bill_amount + 2
    else:
        bill_amount = bill_amount + 3

if extra_cheese == "Y":
    bill_amount = bill_amount + 1
    
print(f"Your total bill amount is ${bill_amount}.")