from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-240, 240)
        self.color("black")
        self.level = 0
        self.write(align="center", font=FONT, arg=f"Level: {self.level}")

    def level_increment(self):
        self.clear()
        self.hideturtle()
        self.level += 1
        self.write(align="center", font=FONT, arg=f"Level: {self.level}")

    def gameover(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write(align="center", font=FONT, arg="GAME OVER")
