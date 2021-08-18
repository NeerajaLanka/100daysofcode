from turtle import Turtle,Screen
import random
turtle_obj_1 = Turtle()
turtle_obj_1.shape("turtle")
turtle_obj_1.pensize(20)
turtle_obj_1.color("black")
turtle_obj_1.speed(50)
colors =["peru","medium violet red","royal blue","red","orange","green","purple"]
b = 300
while b >=1:
    turtle_obj_1.pencolor(random.choice(colors))
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