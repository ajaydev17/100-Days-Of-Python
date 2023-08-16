# this variable is in global scope
enemies_count = 1


def increase_enemy_count():
    # this variable is in local scope, changing this localvariable will not effect the global variable enemies_count

    # we can change the global enemies_count with accessing it inside this function with global keyword
    # global enemies_count

    # but above step is not preferred one because global variables should not be changed inside a local scope

    enemies_count = 2
    # printing the local variable enemies_count
    print(f"Enemies count is: {enemies_count}")


increase_enemy_count()

# this gonna print the global enemies_count variable
print(f"Enemies count is: {enemies_count}")
