MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """
        gonna return whether we can prefer the drink or not with the resources available
    """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry!!, There is not enough {item} make your drink.")
            is_enough = False
    return is_enough


def process_coins():
    """
        returns the total inserted coins
    """
    print("please insert coins!!.")
    total = int(input("How many quarters ? : ")) * 0.25
    total += int(input("How many dimes ? : ")) * 0.1
    total += int(input("How many nickles ? : ")) * 0.05
    total += int(input("How many pennis ? : ")) * 0.01
    return total


is_machine_on = True

while is_machine_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if choice not in MENU:
            print("Not a valid choice!!, please select one of the drinks from the option above")
        else:
            drink_selected = MENU[choice]
            if is_resource_sufficient(drink_selected["ingredients"]):
                print(f"We can prepare the {choice} for you, wait for sometime.")