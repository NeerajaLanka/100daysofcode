import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor=10
        self.y_cor =10
        self.speeds = 0.1
       

    def moves(self):
        new_x = self.xcor()+ self.x_cor
        new_y = self.ycor()+self.y_cor
        self.goto(new_x,new_y)
     
    def bounce_1(self):
        self.y_cor *= -1
        
    
    def bounce_2(self):
        self.x_cor *= -1
        self.speeds *= 0.9
       

    def bounce_3(self):
        self.x_cor *= -1
        self.y_cor  *= 1

    def reset_ball(self):
        self.goto(0,0)
       
