# print some welcome message on the console
print("Welcome to the love calculator...........................................\n")

# ask user for some input
your_name = input("Enter your name: ")
crush_name = input("Enter your crush name: ")

combined_string = your_name.lower() + crush_name.lower()

true = combined_string.count("t") + combined_string.count("r") + \
    combined_string.count("u") + combined_string.count("e")
love = combined_string.count("l") + combined_string.count("o") + \
    combined_string.count("v") + combined_string.count("e")

true_love = int(str(true) + str(love))

if true_love < 10 or true_love > 90:
    print(
        f"Your love score is {true_love}, you go together like coke and mentoes!!")
elif true_love >= 40 and true_love <= 50:
    print(f"Your love score is {true_love}, you are alright together!!")
else:
    print(f"Your love score is {true_love}")
