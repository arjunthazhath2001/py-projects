from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=30
        self.y_move=10
        self.move_speed=0.1

    
    def move(self):
        newx= self.xcor()+self.x_move
        newy= self.ycor()+self.y_move
        self.goto(newx,newy)
    
    
    def ybounce(self):
        self.y_move*=-1
    
    def xbounce(self):
        self.x_move*=-1
        self.move_speed*=0.9

    

    
    def reset(self):
        self.home()
        self.move_speed=0.1
        self.xbounce()
        

