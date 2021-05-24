import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

is_finished = False
while not is_finished:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        is_finished = True
