from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        time.sleep(0.2)
        self.color(random.choice(COLORS))
        self.penup()
        self.speed("slow")
        self.shape("square")
        self.goto(280, random.randint(-280, 280))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)

    def move(self):
        self.setheading(180)
        self.forward(MOVE_INCREMENT)
