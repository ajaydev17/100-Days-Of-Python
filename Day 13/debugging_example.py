from random import randint

# gonna print nothing on the console when you call this function


def my_function():
    for i in range(1, 5):
        if i == 5:
            print("You got it!!")


my_function()

# the above code gonna print nothing because range function excludes the outer boundary to make it work we need include till 6


def my_function():
    for i in range(1, 6):
        if i == 5:
            print("You got it!!")


my_function()


# reproduce the bug with list index out of range

dice_images = ["🔇", "🔕", "🚭", "🚷", "🚯", "🚳"]
dice_number = randint(1, 6)
print(dice_images[dice_number])

# to make the above code proferly we can generate random numbers between 1 to 5

dice_images = ["🔇", "🔕", "🚭", "🚷", "🚯", "🚳"]
dice_number = randint(1, 5)
print(dice_images[dice_number])

# comparison operator
year = int(input("What is your year of birth?: "))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")


# to make the above code proferly we need to put an extra = operator
year = int(input("What is your year of birth?: "))

if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")


# comparing string with integer causes bugs

# age = input("Enter your age: ")
# if age >= 18:
#     print("You can cast vote!!")

# we need to convert age into integer before comparing
age = int(input("Enter your age: "))
if age >= 18:
    print("You can cast vote!!")



# this gonna print 0 on the console
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Bug in the above code is ==

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

