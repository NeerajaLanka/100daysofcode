from turtle import Turtle, xcor, ycor
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list_cars=[]
        self.speeds = STARTING_MOVE_DISTANCE
        
    def new_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(1,2) 
            car.penup()
            y = random.randint(-200,200)
            car.goto(250 , y )
            self.list_cars. append(car)
            car.color(random.choice(COLORS))
        
    def move_car(self) :
        for cars in self.list_cars: 
            cars.backward(self.speeds)
            
    
    def increase_speed(self):
        
            self.speeds += MOVE_INCREMENT 
           




