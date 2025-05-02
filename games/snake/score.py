from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0,280)
        self.write(f"Score: {self.score}",align="center",font=('Arial', 16, 'normal'))

    
    def scoreup(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=('Arial', 16, 'normal'))
