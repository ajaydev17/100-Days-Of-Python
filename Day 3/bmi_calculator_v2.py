# print some welcome mesaage
print("Welcome to the BMI calculator app......................................\n")

# ask user their weight and height
height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg: "))

result = round(weight / height ** 2)

if result < 18.5:
    print(f"Your BMI value is {result}, you are under weight!!")
elif result >= 18.5 and result < 25:
    print(f"Your BMI value is {result}, you have normal weight!!")
elif result >= 25 and result < 30:
    print(f"Your BMI value is {result}, you are over weight!!")
elif result >= 30 and result < 35:
    print(f"Your BMI value is {result}, you are obese!!")
else:
    print(f"Your BMI value is {result}, you are clinically obese!!")