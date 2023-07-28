import random

# print some message on the console
print("Welcome to the Hangman game.........................................................\n")

word_list = ['aardvark', 'baboon', 'camel']

# select a random word from the list
chosen_word = random.choice(word_list)

display = []
for char in chosen_word:
    display += '_'

end_of_game = True

while end_of_game:

    user_guess = input("Guess a letter: ")

    for position in range(len(chosen_word)):
        if user_guess == chosen_word[position]:
            display[position] = user_guess

    print(display)

    if '_' not in display:
        end_of_game = False
        print("You win!!")
