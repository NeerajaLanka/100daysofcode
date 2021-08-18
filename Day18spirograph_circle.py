from turtle import Turtle,Screen
import turtle as t
import random


turtle_obj_1 = t.Turtle()
t.colormode(255)
t.bgcolor("black")


turtle_obj_1.shape("turtle")
turtle_obj_1.speed(20)



def random_color_cir():
    r = random.randint(0,255)
    g  = random.randint(0,255)
    b = random.randint(0,255)
    x = (r,g,b)
    return x
random_color_cir()
a = 50
while a>=1:
    turtle_obj_1.color(random_color_cir())
    turtle_obj_1.circle(100)
    #turtle_obj_1.forward(200)
    turtle_obj_1.left(10)
    turtle_obj_1.tilt(5)
    a-=1
    
screen = Screen()
screen.exitonclick() 