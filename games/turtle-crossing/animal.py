from turtle import Turtle


FINISH_LINE= 250

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(0,-200)
    
    
    def move(self):
        self.forward(20)
