from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(0,-270)


    def move_left(self):
        if  self.xcor() >= -230:
            self.goto(self.xcor()-40, self.ycor())

    def move_right(self):
        if self.xcor() <= 230:
            self.goto(self.xcor()+40, self.ycor())