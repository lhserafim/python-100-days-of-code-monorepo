import random

computer_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {computer_number}")

# A variável foi criada em escopo global
# Caso eu queira alterar uma variável de escopo global dentro de um escopo local, usar: global game_difficulty
game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while game_difficulty not in ("easy", "hard"):
    # Estou acessando a variável global dentro do bloco, pois diferentemente do JAVA o Python não tem escopo de bloco
    game_difficulty = input("You have not chosen a right difficulty. Please type 'easy' or 'hard': ")

if game_difficulty == "easy":
    game_attempts = 10
else:
    game_attempts = 5

is_game_finished = False


def game_attempt():
    global game_attempts
    global is_game_finished # Usei o global, para acessar a variável fora do meu escopo
    game_attempts -= 1
    if game_attempts == 0:
        print("You've run out of guesses, you lose.")
        is_game_finished = True
    else:
        print("Guess again.")
        print(f"You have {game_attempts} attempts remaining to guess the number.")


while not is_game_finished:
    user_guess = int(input("Make a guess: "))
    if user_guess == computer_number:
        print(f"You got it! The answer was {computer_number}.")
        is_game_finished = True
    elif user_guess < computer_number:
        print("Too low.")
        game_attempt()
    else:
        print("Too high.")
        game_attempt()
