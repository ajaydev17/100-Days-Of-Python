import random
import hangman_art
import hangman_words

# print some message on the console
print("Welcome to the Hangman game.........................................................\n")
print(hangman_art.logo)

word_list = hangman_words.word_list

# select a random word from the list
chosen_word = random.choice(word_list)
lives_left = 6

display = []
for char in chosen_word:
    display += '_'

end_of_game = True

while end_of_game:

    user_guess = input("Guess a letter: ")

    if user_guess in display:
        print(f'You have already guessed "{user_guess}".')
    else:
        for position in range(len(chosen_word)):
            if user_guess == chosen_word[position]:
                display[position] = user_guess

    if user_guess not in chosen_word:
        lives_left = lives_left - 1
        print(
            f'You guessed "{user_guess}", which is not in the chosen word, You lose a life!!.')
        print(hangman_art.stages[lives_left])
        if lives_left == 0:
            end_of_game = False
            print(f'You lose!!, The chosen word was "{chosen_word}".')

    if lives_left != 0:
        print(f"{''.join(display)}\n")

    if '_' not in display:
        end_of_game = False
        print("You win!!")
