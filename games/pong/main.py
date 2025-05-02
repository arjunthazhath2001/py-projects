from turtle import Screen,Turtle
import time
from ball import Ball
from midline import Midline

screen= Screen()
screen.bgcolor("black")
screen.title('Pong game')
screen.tracer(0)
screen.setup(width=900, height=600)
screen.listen()

midline=Midline()
ball= Ball()

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)





screen.exitonclick()