from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def read_data():
    with open("data.txt") as file:  # usamos o with para evitar abrir e fechar o arquivo. é uma forma mais prática
        return int(file.read())


def write_data(high_score):
    # mode="w" -> write
    # mode="a" -> append
    with open("data.txt", mode="w") as file:
        file.write(high_score)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_data()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        read_data()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_data(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()













