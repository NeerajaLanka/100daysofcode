from turtle import Turtle,Screen
import random
is_race_on=True
screen = Screen()
screen.setup(width= 500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="guess which turtle gonna win?guess color: ")
colors =["red","green","pink","violet","blue","indigo","orange"]
y_position = [-100,-50,0,50,100,150]
all_turtles =[]
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if user_bet == winning_color :
                print(f"you win,the winning turtle is{winning_color}")
               
            else:
                print(f"you loose,the winning turtle is{winning_color}")
             




screen.exitonclick()