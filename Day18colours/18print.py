import random
from turtle import Turtle
tim = Turtle()
color_list = [(236, 235, 230), (239, 228, 234), (223, 240, 231), (227, 232, 241), (240, 37, 113), (146, 25, 72), (218, 161, 64), (14, 144, 88), (239, 73, 35), (186, 169, 36), (29, 127, 193), (56, 190, 230), (245, 220, 53), (178, 42, 102), (35, 175, 119), (129, 189, 104), (78, 27, 81), (209, 62, 28), (251, 226, 0), (146, 31, 26)]

def random_color():
    r = random.randint(0,255)
    g  = random.randint(0,255)
    b = random.randint(0,255)
    x = (r,g,b)
    tim.color(random.choice(color_list))
    return x
random_color()