import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
player = Player()
screen = Screen()
screen.title("Turtle Cross")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")
i = -1
car = CarManager()
cars = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.append(CarManager())

    for car in cars:
        car.move()
        if player.ycor() == 200:
            scoreboard.level_increment()
            player.restart()

        for car in cars:
            if player.distance(car) < 10:
                scoreboard.gameover()
                game_is_on = False

    screen.update()

screen.exitonclick()
