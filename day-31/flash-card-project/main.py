from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")  # Gera um DataFrame
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
# to_learn = data.to_dict(orient="records")  # Criou uma lista de dicionários.


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)  # Workaround para que o card não vire caso o usuário esteja trocando de cards
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=image_card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=image_card_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)  # coloco para evitar que seja gerado o id do datagrid no csv
    next_card()


window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)  # Espera 3 segundos e vira o card

# Cards
image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file="images/card_back.png")
canvas_image = PhotoImage(file="images/card_front.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(410, 270, image=canvas_image)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 280, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

# Buttons
image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=next_card)
button_right.grid(column=2, row=2)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=is_known)
button_wrong.grid(column=1, row=2)

next_card()

window.mainloop()
