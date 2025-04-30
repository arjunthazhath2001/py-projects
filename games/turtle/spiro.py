from turtle import Turtle, Screen
import random


yertle = Turtle(visible=False)
yertle.speed("fastest")




for i in range(360//10):
    R = random.random()
    B = random.random()
    G = random.random()
    yertle.color(R, G, B)
    yertle.circle(100)
    yertle.setheading(yertle.heading()+10)



screen = Screen()
screen.exitonclick()
