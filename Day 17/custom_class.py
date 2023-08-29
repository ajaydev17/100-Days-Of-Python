# class is a blueprint to create an object
# we can create an empty class with pass keywords

class User:

    # defining the constructor function
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    # class based functions
    def follow(self, user_prof):
        self.following += 1
        user_prof.followers += 1


def my_function():
    """
        empty function example
    """
    pass


user_1 = User("001", "John")
user_2 = User("002", "Smith")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)