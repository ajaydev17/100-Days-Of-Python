# print some message on the console
import random
print(
    "Who will pay the bill??..........................................................\n")


# ask everyone's name
names = input("Give everyone's name seperated by commas!!\n")

names = names.split(',')

# who_will_pay = names[random.randint(0, len(names) - 1)]
who_will_pay = random.choice(names)

print(f"{who_will_pay} is going to pay the bill!!!")
