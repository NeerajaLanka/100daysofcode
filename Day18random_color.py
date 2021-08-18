from turtle import Turtle,Screen
import turtle as t
import random

turtle_obj_1 = t.Turtle()
t.colormode(255)
turtle_obj_1.pensize(5)

def random_color():
    r = random.randint(0,255)
    g  = random.randint(0,255)
    b = random.randint(0,255)
    x = (r,g,b)
    return x
random_color()
b = 300
while b >=1:
    turtle_obj_1.color(random_color())
    a = random.randint(1,4) 
    if a==1:
        turtle_obj_1.forward(25)
    elif a==2:
        turtle_obj_1.backward(25)
    elif a==3:
        turtle_obj_1.left(90)
    elif a==4:
        turtle_obj_1.right(90)
    b -=1

screen = Screen()
screen.exitonclick()