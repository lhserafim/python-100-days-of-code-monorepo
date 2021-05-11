# Importação DICA!
# A importação padrão é como no Java: import turtle
# A importação estática é diferente: from turtle import Turtle

# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

# criando um objeto
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("coral")
my_turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

