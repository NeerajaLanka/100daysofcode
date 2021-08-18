from turtle import Turtle,Screen
import random
import turtle as t
# COLORS = [(236, 235, 230), (239, 228, 234), (223, 240, 231), (227, 232, 241), (240, 37, 113), (146, 25, 72), (218, 161, 64), (14, 144, 88), (239, 73, 35), (186, 169, 36), (29, 127, 193), (56, 190, 230), (245, 220, 53), (178, 42, 102), (35, 175, 119), (129, 189, 104), (78, 27, 81), (209, 62, 28), (251, 226, 0), (146, 31, 26)]
#tim = Turtle()
# def random_color():
#     return random.choice(COLORS)
# tim.dot(20,random_color())
tim = t.Turtle()
t.colormode(255)

#rand_colours = [random.choice(COLORS) for i in range(3)]
COLORS = [(139, 0, 0), 
               (0, 100, 0),
               (0, 0, 139)]
def random_color():
    return random.choice(COLORS) 
for i in range(3):
    tim.dot(20,random_color())
#tim.dot(20,random_color)
screen = Screen()
screen.exitonclick()