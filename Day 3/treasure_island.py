print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Your mission is to find the treasure.")

choice1 = input(
    'You\'re at a crossroad, where you want to go? type "Left" or "Right"\n').lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake, there is an island in the middle. type "Wait" to wait for a boat, type "Swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input(
            'You arrive at the island unharmed, There is a house with three doors. One red, one yellow and one blue. which on do you choose?\n').lower()
        if choice3 == "red":
            print("It is a room full of fire, game over!!")
        elif choice3 == "yellow":
            print("You found the treasure, Hurrahhh You win!!!!")
        elif choice3 == "blue":
            print("You enetered a room of beasts, game over!!")
        else:
            print("You chose a door that does not exists, game over!!")
    else:
        print("You got attacked by an angry trout, game over!!")
else:
    print("You fell into a trap, game over!!")
