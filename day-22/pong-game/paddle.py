from turtle import Turtle


class Paddle(Turtle):
    # The position parameter could be anything. It depends of the caller. In this case I'm passing a tuple
    def __init__(self, position):
        super().__init__()  # Calling the superclass
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # The default size of a turtle is 20. So 20 * 5 = 100
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
