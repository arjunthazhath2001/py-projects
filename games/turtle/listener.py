from turtle import Turtle, Screen
import random


t = Turtle()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)

def move_down():
    t.right(90)

    
def move_left():
    t.left(90)

screen = Screen()
screen.listen()

screen.onkey(key="Right",fun=move_forward)
screen.onkey(key="Left",fun=move_backward)
screen.onkey(key="Up",fun=move_left)
screen.onkey(key="Down",fun=move_down)
screen.exitonclick()
