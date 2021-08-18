from turtle import Screen, up
import time
from create_snake import Snake
from snake_food import Food
from score_board1 import Scoreboard
 
food = Food()
snake = Snake()
scores = Scoreboard()


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend_snake()
        scores.increment()
    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        scores.prints()
        game_is_on = False 
    #detect collision with tail
    for i in snake.segment[1:]:
        
        if  snake.head.distance(i) < 10:
            game_is_on = False 

            scores.prints()

    
            

        
        
        

    


screen.exitonclick()