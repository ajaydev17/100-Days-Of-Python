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
        print(f"You got it right!!, the answer was {answer}")

# sets the difficulty of the game.


def set_difficulty():
    choice = input("hoose your difficulty. Type 'easy' or 'hard': ")
    if choice == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
