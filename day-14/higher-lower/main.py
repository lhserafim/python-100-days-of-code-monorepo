import random
from art import logo, vs
from game_data import data

# Global Variables
score = 0
is_game_finished = False


def print_compare(p_type, p_name, p_description, p_country):
    print(f"Compare {p_type}: {p_name}, a {p_description} from {p_country}.")


def add_score():
    global score
    score += 1


def check_answer(p_follower_count_a, p_follower_count_b):
    global is_game_finished
    if p_follower_count_a < p_follower_count_b:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_finished = True
    else:
        add_score()
        print(f"You're right! Current score: {score}.")


def game():
    while not is_game_finished:
        follower_count_a = 0
        follower_count_b = 0

        print(logo)
        random_choice = random.choice(data)
        follower_count_a = random_choice["follower_count"]
        print_compare("A", random_choice["name"], random_choice["description"], random_choice["country"])

        print(vs)
        random_choice = random.choice(data)
        follower_count_b = random_choice["follower_count"]
        print_compare("B", random_choice["name"], random_choice["description"], random_choice["country"])

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        while answer not in ("A", "B"):
            answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        check_answer(follower_count_a, follower_count_b)


game()

