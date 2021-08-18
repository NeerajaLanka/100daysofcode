from turtle import Turtle,Screen
import random
turtle_obj_1 = Turtle()
colors =["olive green","peru","medium violet red","royal blue","red","orange","green","purple"]
def shapes(sides):
    angle = 360/sides
    for _ in range(sides):
        turtle_obj_1.forward(100)
        turtle_obj_1.right(angle)
for i in range(3,11):
    turtle_obj_1.color(random.choice(colors))
    shapes(i)
screen = Screen()
screen.exitonclick()