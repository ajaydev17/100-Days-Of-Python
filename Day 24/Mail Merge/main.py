# get starting letter
with open('./Input/Letters/starting_letter.txt', mode="r") as file:
    content = file.read()

# get all the names
with open('./Input/Names/invited_names.txt', mode="r") as names:
    all_names = names.read().split('\n')

for name in all_names:
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode="w") as output:
        output.write(content.replace('[name]', f'{name}'))
