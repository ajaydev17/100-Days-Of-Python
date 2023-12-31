import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect player collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    if player.is_player_finished():
        player.reset_position()
        car_manager.increase_speed()
        score_board.update_score()


screen.exitonclick()
