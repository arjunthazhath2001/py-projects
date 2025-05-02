from turtle import Turtle

STARTING_POSITIONS= [(0,0),(20,0),(-20,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self):  
        self.segments=[]
       
        for pos in STARTING_POSITIONS:
            new_seg= Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(pos)
            self.segments.append(new_seg)
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x= self.segments[seg_num-1].xcor()
            new_y= self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)