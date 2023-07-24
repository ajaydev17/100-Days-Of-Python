# print something on the console
print("Welcome to the highest score finder")

all_scores = input("Please enter all the scores seperated by spaces: ")
all_scores = all_scores.split(" ")

# this is one way of doing it using built in functions
all_scores = [int(score) for score in all_scores]
high_score = max(all_scores)
print(f"Highest score is : {high_score}")

# this is the second way of doing it using for loops
high_score = 0
for score in all_scores:
    if score > high_score:
        high_score = score

print(f"Highest score is : {high_score}")
