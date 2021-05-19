import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict()) # neste caso não vai nos atender

# MODO 1
new_dict = {}
for (index, row) in data.iterrows():
    new_dict[row.letter] = row.code

print(new_dict)

# MODO 2 (MELHOR!)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("What is the word? ").upper()
letter_list = [new_dict[letter] for letter in user_word]  # Combinando lista e dicionário
print(letter_list)



