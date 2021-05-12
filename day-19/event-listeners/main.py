from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


screen.listen()

# Quando passamos uma função como parâmetro não colocamos o (), só passamos o nome da função
screen.onkey(fun=move_forwards, key="space")

screen.exitonclick()
