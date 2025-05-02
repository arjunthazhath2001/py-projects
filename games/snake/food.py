from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
        
    def refresh(self):
        randomx= random.randint(-230,230)
        randomy= random.randint(-230,230)
        self.goto(randomx,randomy)
    
