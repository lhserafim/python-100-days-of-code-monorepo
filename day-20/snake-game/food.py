from turtle import Turtle
import random


# Turtle é a superclasse. A maneira que fazemos herança em Python é colocando a superclasse dentro de ()
class Food(Turtle):

    def __init__(self):
        super().__init__()  # É recomendado utilizar o super(), quando fazemos herança mas não é obrigatório
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
