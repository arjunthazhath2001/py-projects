from turtle import Turtle,Screen
import random

screen= Screen()

screen.colormode(255)
MOVE_DISTANCE=5
INC_MOVE_DISTANCE=5



class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.segments = []
    
    def create_car(self):
        random_chance= random.randint(1,6)
        if random_chance==1:
            new_seg= Turtle("square")
            r= random.randint(0,255)
            g=random.randint(0,255)
            b= random.randint(0,255)
            new_seg.fillcolor((r, g, b))
            
            new_seg.shapesize(stretch_wid=1, stretch_len=2)
            new_seg.penup()
            new_seg.seth(180)
            # new_x= random.randint(300)
            new_y= random.randint(-150,150)
            new_seg.goto(300,new_y)
            self.segments.append(new_seg)

        
    
    def move(self):
        for seg in self.segments:
            seg.forward(MOVE_DISTANCE)
            
    
    def refresh(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE+= INC_MOVE_DISTANCE
            
