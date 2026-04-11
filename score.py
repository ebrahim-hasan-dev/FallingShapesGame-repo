from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_bord()

    def score_bord(self):
        self.goto(0,250)
        self.write(f"Score : {self.score}",font=("Arial",20,"normal"),align="center")
        

    def score_increase(self):
        self.clear()
        self.score_bord()

    def game_over(self):
        r = Turtle()
        r.goto(0,0)
        r.color("white")
        r.hideturtle()
        r.write("Game Over",font=("Arial",30, "normal"),align="center")
        
