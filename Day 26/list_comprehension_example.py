import random
import pandas
# squaring the numbers

number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

squared_numbers = [number * number for number in number_list]
print(squared_numbers)

# filtering out even numbers

even_numbers = [number for number in squared_numbers if number % 2 == 0]
print(even_numbers)

# filtering out odd numbers

odd_numbers = [number for number in squared_numbers if number % 2 != 0]
print(odd_numbers)

# dictionary comprehension

example_string = "What is the Airspeed velocity of an Unladen Swallow?"
example_string_list = example_string.split(" ")

example_dict = {str(element): int(len(element)) for element in example_string_list}
print(example_dict)

students = ["Alex", "Beth", "John", "Chris", "Jordan", "Stewart"]
student_score_dict = {str(name): int(random.randint(1, 100)) for name in students}
print(student_score_dict)

# get the students who got passing marks i.e >= 35

passed_students = {str(name): int(score) for name, score in student_score_dict.items() if int(score) >= 35}
print(passed_students)

# iterate over the pandas DataFrame

dataframe_data = pandas.DataFrame([passed_students])
print(dataframe_data)

print("---------------------------------------------------------------------------------------------------------------")

for index, row in dataframe_data.iterrows():
    print(index, row)



