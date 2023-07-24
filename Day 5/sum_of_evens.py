# print something on the console
print("Sum of even numbers from 1 to 100..............................\n")

# this is the one way with step count of 2
total_sum = 0
for number in range(2, 101, 2):
    total_sum += number
print(f"Total sum of even numbers from 1 to 100 is : {total_sum}")

# this is the 2nd way of doing it by checking even number or not
total_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_sum += number
print(f"Total sum of even numbers from 1 to 100 is : {total_sum}")
