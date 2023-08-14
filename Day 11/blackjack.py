import random


def deal_card():
    """
        Returns a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
        Returns the sum of a list
    """

    # if length of the cards list is 2 and sum is 21 return 0
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    # if ace in the cards list and sum is greater than 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_scores(user_score, computer_score):
    """
        compares user score and computer score, returns the winner.
    """

    if user_score > 21 and computer_score > 21:
        return "You went over, you lose🤧"

    if user_score == computer_score:
        return "It's a Draw🙃"
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack😱"
    elif user_score == 0:
        return "You win, with a Blackjack😎"
    elif user_score > 21:
        return "You went over. You lose😭"
    elif computer_score > 21:
        return "Opponent went over. You win😁"
    elif user_score > computer_score:
        return "You win😃"
    else:
        return "You lose😤"


def play_game():
    """
        starts the blackjack game.
    """

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(
            f"   Your cards are: {user_cards}, current score is: {user_score}")
        print(f"   Computers card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")

            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
