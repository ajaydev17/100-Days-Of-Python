# print some welcome message on the console
import random
print(
    "Welcome to head or toss predictor app.........................................................\n")


# generates random numner between 0 and 1
random_number = random.randint(0, 1)

if random_number == 1:
    print("It is HEAD!!")
else:
    print("It is TAILS!!")
