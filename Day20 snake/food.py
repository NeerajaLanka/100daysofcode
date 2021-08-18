from turtle import Turtle, circle
import turtle
import random

class Food(Turtle):
    def __init__(self, shape: circle):
        super().__init__()
        self.penup()
        self.circle(5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x =random.randint(-280,280)
        random_y =random.randint(-280,280)
        self.goto(random_x, random_y)