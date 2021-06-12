import random
from flask import Flask

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


# criando decorators
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def gif_number(function):
    def wrapper():
        return function() + "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    return wrapper


# def def_gif_answer(function):
#     def wrapper(*args, **kwargs):
#         print(args[0])
#     return wrapper


# High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif
# Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif
# Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif


@app.route("/")
@make_bold
@gif_number
def home():
    return "Guess a number between 0 and 9"


# convertendo p/ int
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
