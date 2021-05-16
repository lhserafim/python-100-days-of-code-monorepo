# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_names():
    with open("./Input/Names/invited_names.txt") as file:
        names = file.readlines()
        return names


def read_letter(names):
    with open("./Input/Letters/starting_letter.txt") as file:
        letter = file.read()
        for name in names:
            write_file(letter.replace("[name]", name.strip()), name)


def write_file(letter, name):
    path = f"./Output/ReadyToSend/{name.strip()}.txt"
    with open(path, mode="w") as file:
        file.write(letter)


names = read_names()
read_letter(names)
