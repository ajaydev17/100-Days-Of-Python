# example for positional argument
def print_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}, How are you doing today?!")


print_name("Ajay", "Devadiga")

# example for keyword argument


def print_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}, How are you doing today?!")


print_name(last_name="Ajay", first_name="Devadiga")

# you can define function again with the same name, its gonna override
