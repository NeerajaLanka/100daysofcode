import time
from turtle import Screen, exitonclick, up
from player import Player
from car_manager import CarManager
from scoreboard import Score_board

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player_1 = Player()
carmanager = CarManager()
scoreboard = Score_board()


screen.listen()
screen.onkey(player_1.move_north,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.new_car()
    carmanager.move_car()

    #detect collision with car
    for cars_all in carmanager.list_cars:
        if cars_all.distance(player_1) < 20:
            game_is_on = False
            scoreboard.end_game()
    #detect final position
    if player_1.final_position():
        carmanager.increase_speed()
        scoreboard.level_increment()
      
       
        


exitonclick()

