# print some welcome message on the console
print("Welcome to the treasure map...............................................\n")

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

# ask user where they want to place the treasure
position = input("Where you wanna put your treasure? : ")

row = int(position[0]) - 1
column = int(position[1]) - 1

treasure_map[row][column] = 'X'
print(f"{row1}\n{row2}\n{row3}\n")
