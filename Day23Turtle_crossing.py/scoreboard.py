from turtle import Screen, Turtle
FONT = ("Courier", 24, "normal")


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.color("black")
        self.levels = 1
        self.updates()
       
        
    def level_increment(self):
        
        self.levels += 1
        self.clear()
        self.updates()
    def updates(self):
        self.write(f"level: {self.levels}", align ="center",font=FONT)
    
    def end_game(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

    
