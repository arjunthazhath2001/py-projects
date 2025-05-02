from turtle import Turtle,Screen

screen= Screen()
screen.bgcolor("black")
screen.title('Snake game')


starting_pos= [(0,0),(20,0),(-20,0)]

# screen.tracer(0)
segments=[]

for pos in starting_pos:
    new_seg= Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(pos)
    segments.append(new_seg)

game_is_on=True

while game_is_on:
    for seg in segments:
        seg.forward(20)
        screen.update()
















screen.exitonclick()