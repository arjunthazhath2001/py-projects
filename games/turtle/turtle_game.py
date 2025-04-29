import random
from turtle import Turtle, Screen

timmy= Turtle()


for side in range(3,11):
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)
    for i in range(side):
        timmy.forward(100)
        timmy.left(360//side)


screen= Screen()
screen.exitonclick()