# this is a function takes first_name, last_name as input
# and returns formatted name as output
def format_name(first_name, last_name):
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"{formatted_first_name} {formatted_last_name}"


formatted_name = format_name("aJaY", "dEVaDIgA")
print(formatted_name)
