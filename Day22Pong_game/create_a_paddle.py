from turtle import Turtle, xcor, ycor



class Paddle_1(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
         
        self.hideturtle()
        self.shape("square")
        self.shapesize(1,5)
        self.color("white")
        self.penup()
        self.goto(xcor,ycor)
        
        self.showturtle()
        self.setheading(90)
        
        
        
            
    def move_up(self):
        news_y = self.ycor()+20
        self.goto(self.xcor(),news_y)
        
        
    def move_down(self):
        news_y = self.ycor()-20
        self.goto(self.xcor(),news_y)



     
        
          
