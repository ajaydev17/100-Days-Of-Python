# print some welcome message
print("Welcome to the tip calculator app......................................!!\n")

total_amount = float(input("Enter the total bill amount : "))
tip_percentage = int(input("Enter the tip percentage like 5, 10 or 15? : "))

tip_amount = total_amount * tip_percentage / 100
total_bill = total_amount + tip_amount

total_people = int(input("Enter the total number of people : "))

bill_per_person = total_bill / total_people

print(f"The amount to be paid per person is : ${bill_per_person}")