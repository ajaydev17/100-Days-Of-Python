import random

# print some message on the console
print("Welcome to Python Password Generator.................................................\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '+', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '?', '<', '>', '`', '~', '_', '"', "'", '\\']


number_of_letters = int(
    input("How many number would you like in your password : "))
number_of_numbers = int(
    input("How many numbers would you like in your password : "))
number_of_symbols = int(
    input("How many symbols would you like in your password : "))

password_list = []

for letter in range(1, number_of_letters + 1):
    password_list += random.choice(letters)

for number in range(1, number_of_numbers + 1):
    password_list += random.choice(numbers)

for symbol in range(1, number_of_symbols + 1):
    password_list += random.choice(symbols)

password = ""
random.shuffle(password_list)
for char in password_list:
    password += char

print(f"Your password is : {password}")
