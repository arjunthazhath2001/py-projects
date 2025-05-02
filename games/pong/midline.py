from turtle import Turtle

class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self= Turtle()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.pensize(5)
        self.setposition(0,310)
        self.seth(270)

        for _ in range(600//20):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
