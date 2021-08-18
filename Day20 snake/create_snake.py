from turtle import Turtle,Screen, up
import time
import random
import turtle


# screen = Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")

SEGMENT_FORWARD= 20
NEW_SEGMENT=[(0,0),(-20,0),(-40,0)]
Up= 90
Down = 270
Left = 180
Right = 0

class Snake:
   
    def __init__(self):
        
        self.segment =[ ]
       
        self.snake_large()
        self.head = self.segment[0]
    def add_segment(self,i):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.segment.append(tim)
       

    def snake_large(self):
        for i in NEW_SEGMENT:
           self.add_segment(i) 
    def extend_snake(self):
            self.add_segment(self.segment[-1].position())
    
    
    
    
    def move(self):
        for seg_num in range((len(self.segment)-1),0,-1):
            new_x = self.segment[ seg_num -1].xcor()
            new_y = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(SEGMENT_FORWARD)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)
        
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)


    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)
    
    def right(self): 
        if self.head.heading() != Left:
            self.head.setheading(Right)
    

    




   








