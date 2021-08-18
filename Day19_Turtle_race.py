from turtle import Turtle,Screen
import random
import turtle as t
t.colormode(255)
tig = Turtle()
tog = Turtle()
log = Turtle()
jog = Turtle()
rog = Turtle()
mog = Turtle()
def first(): 
    tig = Turtle(shape="turtle")
    tig.penup()
    tig.goto(x=-230,y=-100)
    tig.color(colors[i])

def second():
    tog = Turtle(shape="turtle")
    tog.penup()
    tog.goto(x=-230,y=-50)
    tog.color(colors[i])
def third():
    log = Turtle(shape="turtle")
    log.penup()
    log.goto(x=-230,y=-0)
    log.color(colors[i])
def fourth():
    jog = Turtle(shape="turtle")
    jog.penup()
    jog.goto(x=-230,y=50)
    jog.color(colors[i])
def fifth():
    rog = Turtle(shape="turtle")
    rog.penup()
    rog.goto(x=-230,y=100)
    rog.color(colors[i]) 
def sixth():
    mog = Turtle(shape="turtle")
    mog.penup()
    mog.goto(x=-230,y=150)
    mog.color(colors[i])  

screen = Screen()
screen.setup(width= 500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="guess which turtle gonna win?guess color: ")
colors =["red","green","pink","violet","blue","indigo","orange"]
for i in range(6):
    if i==0:
        first()
        
    elif i==1:
        second()
        
    elif i==2:
        third()
        
    elif i==3:
        fourth()
        
    elif i==4 :
        fifth()
        
    elif i==5:
        sixth()    
    
screen.exitonclick()