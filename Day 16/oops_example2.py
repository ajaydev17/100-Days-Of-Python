from prettytable import PrettyTable

# creating an object
table = PrettyTable()

# accessing the methods on the object
table.add_column("Player Name", ["zlatan ibrahimovic", "Cristiano Ronaldo", "Lionel Messi"])
table.add_column("Goals Scored", [17, 29, 50])
table.align = "l"
print(table)