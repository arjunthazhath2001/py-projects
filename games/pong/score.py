from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        if pos=="left":
            self.setposition(-80,200)
        else:
            self.setposition(80,200)
        self.write(f"{self.score}",align="center",font=("Futura", 50, 'bold'))

    
    def scoreup(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}",align="center",font=("Futura", 50, "bold"))


    def gameover(self):
        self.setposition(0,0)
        self.write("Game over",align="center",font=('Arial', 16, 'normal'))

