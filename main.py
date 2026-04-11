from turtle import Screen
from score import Score
from player import Player
from shapes import Shapes
import time

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Falling Shapes Game")

score = Score()
player = Player()
shape = Shapes()

shape_speed = 0.1
game_on = True

screen.listen()
screen.onkeypress(player.move_left,"Left")
screen.onkeypress(player.move_right,"Right")

while game_on:
    shape.falling()
    screen.update()
    time.sleep(shape_speed)
    
    if player.distance(shape) <= 50:

        shape_color = shape.color()[0]
        shape_type = shape.shape()

        if shape_type == "circle":
            score.score += 1

        elif shape_type == "square":
            score.score += 2

        elif shape_type == "triangle":
            score.score = 0

        elif shape_type == "turtle":
            if shape_color == "white":
                score.game_over()
                game_on= False
            else:
                score.score += 5
        
        score.score_increase()
        shape.firt_move()
        shape.shapes_and_colors_and_sizes()

        if shape_speed > 0.05:
            shape_speed -= 0.01
        
screen.exitonclick()