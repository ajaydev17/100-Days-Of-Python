import random

# print some message on the console
print("Welcome to the Hangman game.........................................................\n")

stages = ['''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
 
''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
 
''', '''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
 
''', '''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
 
''', '''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========
 
''', '''
 
  +---+
  |   |
      |
      |
      |
      |
=========
 
''']

word_list = ['aardvark', 'baboon', 'camel']

# select a random word from the list
chosen_word = random.choice(word_list)
lives_left = 6

display = []
for char in chosen_word:
    display += '_'

end_of_game = True

while end_of_game:

    user_guess = input("Guess a letter: ")

    for position in range(len(chosen_word)):
        if user_guess == chosen_word[position]:
            display[position] = user_guess
    else:
        lives_left = lives_left - 1
        if lives_left == 0:
            end_of_game = False
            print("You lose!!")

    print(f"{''.join(display)}")

    if '_' not in display:
        end_of_game = False
        print("You win!!")
