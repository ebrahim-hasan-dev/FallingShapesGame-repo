from turtle import Turtle
import random

class Shapes(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.colors = ["red", "blue", "white", "purple", "yellow", "cyan", "orange", "brown", "pink", "white", "white"]
        self.shapes = ["square", "turtle", "triangle", "circle", "turtle", "turtle"]
        self.firt_move()
        self.shapes_and_colors_and_sizes()
        
    def firt_move(self):
        self.goto(random.randint(-280,280), 300)##
        

    def shapes_and_colors_and_sizes(self):
        if self.ycor() == 300:
            self.color(random.choice(self.colors)) 
            self.shape(random.choice(self.shapes))
            rand = random.uniform(0.3,2)## uniform = عشوائي flaot بتختار رقم 
            self.shapesize(stretch_len=rand, stretch_wid=rand) 
            
    
    def falling(self):
        self.goto(self.xcor(), self.ycor()-20)

        if self.ycor() < -300:
            self.firt_move()
            self.shapes_and_colors_and_sizes()

    
        
        