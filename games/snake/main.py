from turtle import Turtle,Screen

screen= Screen()
screen.bgcolor("black")
screen.title('Snake game')


starting_pos= [(0,0),(20,0),(-20,0)]


for pos in starting_pos:
    new_seg= Turtle("square")
    new_seg.color("white")
    new_seg.goto(pos)


screen.exitonclick()