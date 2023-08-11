logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


def find_highest_bid(bid_information):
    highest_bid_amount = 0
    bid_winner = ''
    for bidder in bid_information:
        current_bid_amount = bid_information[bidder]
        if current_bid_amount > highest_bid_amount:
            highest_bid_amount = current_bid_amount
            bid_winner = bidder
    print(f"The winner is {bid_winner} with a bid of ${highest_bid_amount}")


is_bid_finished = False

while not is_bid_finished:
    bid_info = {}
    name = input("please provide the bidder name: ")
    bid_amount = int(input("please provide the bid amount $: "))
    bid_info[name] = bid_amount

    continue_bid = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if continue_bid == "no":
        is_bid_finished = True
        find_highest_bid(bid_information=bid_info)
