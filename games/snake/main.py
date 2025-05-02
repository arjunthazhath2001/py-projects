from turtle import Turtle,Screen
import time
screen= Screen()
screen.bgcolor("black")
screen.title('Snake game')


starting_pos= [(0,0),(20,0),(-20,0)]

screen.tracer(0)
segments=[]

for pos in starting_pos:
    new_seg= Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(pos)
    segments.append(new_seg)

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(len(segments)-1,0,-1):
        new_x= segments[seg_num-1].xcor()
        new_y= segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
















screen.exitonclick()