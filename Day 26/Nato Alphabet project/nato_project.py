import pandas as pd

# reading the csv file
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alphabet)

# nato_phonetic_alphabet = nato_alphabet.to_dict()
# print(nato_phonetic_alphabet)

# create a dictionary in a proper format
nato_phonetic_alphabet_dict = {row.letter: row.code for index, row in nato_alphabet.iterrows()}
# print(nato_phonetic_alphabet_dict)


def generate_nato_phonetic_alphabet():
    user_input = input("Enter your word: ").upper()

    try:
        nato_code = [nato_phonetic_alphabet_dict[word] for word in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet!!")
        generate_nato_phonetic_alphabet()
    else:
        print(nato_code)


generate_nato_phonetic_alphabet()


# another way of doing it with pandas item methods

# df = pd.read_csv('nato_phonetic_alphabet.csv')
#
# # nato_code_dict = {row.letter : row.code for (index, row) in df.iterrows() }
#
# user_input = input('enter a word:  ').upper()
# # nato_code = [nato_code_dict[letter] for letter in user_input]
# nato_code = [df.code[df.letter == letter].item() for letter in user_input]
# print(nato_code)
