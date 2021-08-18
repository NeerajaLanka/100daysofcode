from turtle import Turtle,Screen, color
import random
import turtle as t

# rgb_colors =[]
# colors = colorgram.extract('image.jpg',20)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r,g,b)
#     rgb_colors .append(new_color)
# print(rgb_colors )
COLORS = [(236, 235, 230), (239, 228, 234), (223, 240, 231), (227, 232, 241), (240, 37, 113), (146, 25, 72), (218, 161, 64), (14, 144, 88), (239, 73, 35), (186, 169, 36), (29, 127, 193), (56, 190, 230), (245, 220, 53), (178, 42, 102), (35, 175, 119), (129, 189, 104), (78, 27, 81), (209, 62, 28), (251, 226, 0), (146, 31, 26)]
tim = t.Turtle()
t.colormode(255)
x = -200
y = -200
def random_color():
    return random.choice(COLORS)

while True:
    tim.penup()
    tim.goto(x,y)
    tim.pendown()
    for i in range(10):
        tim.dot(20,random_color())
        tim.penup()
        tim.forward(50)
        tim.pendown()
    y = y+50
    if y== 300:
        break
    tim.hideturtle()

screen = Screen()
screen.exitonclick()


