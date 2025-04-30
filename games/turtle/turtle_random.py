import random
from turtle import Turtle, Screen

timmy= Turtle()




timmy.pensize(5)
timmy.speed(10)
directions=[0,90,180,270]

for side in range(100):
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen= Screen()
screen.exitonclick()