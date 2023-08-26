from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating the objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# start the coffee machine
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have? ({options}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        selected_drink = menu.find_drink(choice)
        if selected_drink is not None and coffee_maker.is_resource_sufficient(selected_drink) and \
                money_machine.make_payment(selected_drink.cost):
            coffee_maker.make_coffee(selected_drink)
