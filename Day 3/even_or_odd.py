# print some welocme message
print("Welcome to even or odd predictor!!!............................................\n")

# aks user for their number
number = int(input("Enter your number: "))

if number % 2 == 0:
    print(f"The entered number {number} is even")
else:
    print(f"The entered number {number} is odd")