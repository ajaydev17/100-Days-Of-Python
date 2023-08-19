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
