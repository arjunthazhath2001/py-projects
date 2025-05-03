from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.hideturtle()
        self.penup()
        self.setposition(-190,200)
        self.write(f"Level: {self.score}",align="center",font=('Arial', 16, 'normal'))

    
    def scoreup(self):
        self.score+=1
        self.clear()
        self.write(f"Level: {self.score}",align="center",font=('Arial', 16, 'normal'))


    def gameover(self):
        self.setposition(0,0)
        self.write("Game over",align="center",font=('Arial', 16, 'normal'))

