from turtle import Turtle
score = 0
class scoreboard(Turtle):
   def __init__(self,score):
        self.write("score_board",move=False,align="middle",font=12)
        
        score+=1
