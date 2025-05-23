from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
       
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if pos=="left":
            self.goto(-420,0)
        else:
            self.goto(420,0)
    
    def moveup(self):
        new_y= self.ycor()+20
        self.goto(self.xcor(),new_y)
    
    def movedown(self):
        new_y= self.ycor()-20
        self.goto(self.xcor(),new_y)
       
        