from ball_pong import Ball
from create_a_paddle import Paddle_1
from turtle import Turtle,Screen, exitonclick, xcor, ycor
import time
from score_boards import Score_board
tim = Turtle()
screen = Screen()



screen.bgcolor("black")
tim.color("white")
tim.shape("square")
screen.setup(width=800,height=600)
screen.title("pong")
tim.penup()
tim.goto(0,580)
tim.setheading(270)
tim.pensize(5)

for _ in range(90):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)



l_paddle = Paddle_1(-350,0)
r_paddle = Paddle_1(350,0)
score_board = Score_board()

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")

screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
ball= Ball()
game_is_on = True
while game_is_on :
    time.sleep(ball.speeds)
    #screen.update()
    ball.moves()
    #wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_1()
    #collision with paddles
    if  ball.xcor() > 340 and ball.distance(r_paddle) < 50 or  ball.xcor() < -340 and  ball.distance(l_paddle) < 50:
        ball.bounce_2()
    #detect when r_paddle misses
    if  ball.xcor() > 360 :
        ball.reset_ball()
        ball.bounce_3()
        score_board.r_point()
        
    #detect when l_paddle misses 
    if  ball.xcor() < -360 : 
        ball.reset_ball()
        ball.bounce_3()
        score_board.l_point()

    

      

exitonclick()
