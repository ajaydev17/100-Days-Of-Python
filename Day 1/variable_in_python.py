# python variable and f string example

name = input("What is your name? : ")
length = len(name)
print(f"Your name contains {length} letters")

# example to swap value stored in two variables

a = input("Enter the value of a : ")
b = input("Enter the value of b : ")

temp = a
a = b
b = temp

print(f"Now the value of a is : {a}")
print(f"Now the value of b is : {b}")