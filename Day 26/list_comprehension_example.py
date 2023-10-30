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

example_dict = {str(element):int(len(element)) for element in example_string_list}
print(example_dict)



