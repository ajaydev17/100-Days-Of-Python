# print some message on the console
import random
print("Random number generator.........................................\n")


print("Prints random number between 1 and 100")
print(random.randint(1, 100))

print("Prints random number between 100 and 200")
print(random.randrange(100, 200))

print("both randint and randrange work almost same!!!")

print("Prints random number between 0 and 5")
print(int(random.random() * 5))
