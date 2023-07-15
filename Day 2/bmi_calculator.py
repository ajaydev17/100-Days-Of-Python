# print some welcome message
print("Welcome to the BMI calculator app")

# ask for user inputs
height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in Kg: "))

result = int(weight / height ** 2)

# print out the result
print(f"Your BMI calculation is : {result}")
