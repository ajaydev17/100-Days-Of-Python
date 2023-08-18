from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo = """
  _____                       _______ _            _   _                 _               _ _ 
  / ____|                     |__   __| |          | \ | |               | |             | | |
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __| | |
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | |
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|_|
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_|_)
"""

# function to check users guess against actual asnwer


def check_answer(guess, answer, turns):
    """
        checks users guess against actual asnwer, returns the number turns remaining
    """
    if guess > answer:
        print("Too hight!!")
        return turns - 1
    elif guess < answer:
        print("Too low!!")
        return turns - 1
    else:
        print(f"You got it right!!, the answer was {answer}!!")

# sets the difficulty of the game.


def set_difficulty():
    choice = input("Choose your difficulty. Type 'easy' or 'hard': ")
    if choice == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)

    print("Welcome to the number guessing game!!!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again!!")


game()
