from turtle import Turtle

STARTING_POSITIONS= [(0,0),(20,0),(-20,0)]
MOVE_DISTANCE=20
LEFT=180
RIGHT=0
UP=90
DOWN=270

class Snake:
    def __init__(self):  
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]
    

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
    
    def add_segment(self,pos):
        new_seg= Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head= self.segments[0]

    
    def extend(self):
        self.add_segment(self.segments[-1].pos())


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x= self.segments[seg_num-1].xcor()
            new_y= self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.seth(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.seth(LEFT)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.seth(RIGHT)