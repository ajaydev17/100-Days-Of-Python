enemies_count = 1


def increase_enemy_count():
    # will print the global enemeies count
    print(f"Enemies count is: {enemies_count}")

    # returns the global enemeies count + 1
    # this is preferred way of updating the global variables
    return enemies_count + 1


# the global enemies count will be increased by 1
enemies_count = increase_enemy_count()

# prints the updated global enemeies count
print(f"Enemies count is: {enemies_count}")
