import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

is_invalid = False
computer_choice = random.randint(1, 3)
choice = [int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))]

# Só para "brincar" transformei em uma lista para poder validar usando NOT IN. Poderia ter usado or
# if choice != 1 or != 2 or != 3:
# https://www.w3schools.com/python/python_operators.asp

for x in choice:
    if not x in (1, 2, 3):
        is_invalid = True

if not is_invalid:
    if choice[0] == 1:
        print(rock)
    elif choice[0] == 2:
        print(paper)
    else:
        print(scissors)

    print("Computer has chosen")
    if computer_choice == 1:
        print(rock)
    elif computer_choice == 2:
        print(paper)
    else:
        print(scissors)

    if choice[0] == computer_choice:
        print("Game tied")
    elif choice[0] == 1 and computer_choice == 2:
        print("You Lost")
    elif choice[0] == 1 and computer_choice == 3:
        print("You Win")
    elif choice[0] == 2 and computer_choice == 1:
        print("You Win")
    elif choice[0] == 2 and computer_choice == 3:
        print("You Lost")
    elif choice[0] == 3 and computer_choice == 1:
        print("You Lost")
    elif choice[0] == 3 and computer_choice == 2:
        print("You Win")
else:
    print("The chosen number is invalid!")







