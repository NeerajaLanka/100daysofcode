from turtle import Turtle,Screen
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


new_segment=[(0,0),(-20,0),(-40,0)]
segment =[ ]

for i in new_segment:
    tim = Turtle("turtle")
    tim.color("white")
    tim.penup()
    tim.goto(i)
    segment.append(tim)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for seg_num in range((len(segment)-1),0,-1):
        new_x = segment[ seg_num -1].xcor()
        new_y = segment[seg_num -1].ycor()
        segment[seg_num].goto(new_x,new_y)
    segment[0].forward(20)
    segment[0].left(90)




screen.exitonclick()
