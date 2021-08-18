from turtle import Turtle, clear



file = open("/Users/prasadkundeti/Desktop/score_data.txt") 
content =file.read()
print(content)
file.close()






ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore =int(content)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} high score:{self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def resets(self):
        if self.score  > int(content):
            self.highscore = self.score
            file = open("/Users/prasadkundeti/Desktop/score_data.txt",mode = "w")
            file.write(f"{self.score}")
        self.score= 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
       
