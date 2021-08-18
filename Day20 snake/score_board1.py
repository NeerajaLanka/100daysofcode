from turtle import Turtle

class Scoreboard(Turtle):
   
   def __init__(self):
       super().__init__()
       self.penup()
       self.hideturtle()
       self.goto(0,270)
       self.color("white")
       self.score = 0
       self.update_score()
    
   def update_score(self):
       self.write(f"score_board :{self.score}",align="center",font=("Arial",12,"normal"))
       
   def increment(self):  
        self.score+=1
        self.clear()
        self.update_score()

   def prints(self):
        self.color("white")
        self.goto(0,0)
        self.write("game over",align="center",font=("Arial",16,"normal"))
    




        
  
