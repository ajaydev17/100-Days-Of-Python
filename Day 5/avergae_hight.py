# print some message on the console
print("Welcome to average hight finder!!")

all_heights = input("Please enter all the heights seperated by space: ")
all_heights = all_heights.split(" ")


# this is one way of doing it using built in modules
all_heights = [int(height) for height in all_heights]

sum_of_heights = sum(all_heights)
total_heights = len(all_heights)

average_height = round(sum_of_heights / total_heights)

print(f"The average height of the class is {average_height}cms.")


# the second way of doing it using for loops
sum_of_heights = 0
total_heights = 0
for height in all_heights:
    sum_of_heights = sum_of_heights + height
    total_heights = total_heights + 1

average_height = round(sum_of_heights / total_heights)
print(f"The average height of the class is {average_height}cms.")
