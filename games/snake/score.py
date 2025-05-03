from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.highscore= int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,200)
        self.update_score()
      
    def update_score(self):
       
                
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align="center",font=('Arial', 16, 'normal'))

    
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore= self.score
            with open("data.txt",'w') as file:
                item= str(self.highscore)
                file.write(item)
        self.score=0
        self.update_score()
    
    
        
    def scoreup(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align="center",font=('Arial', 16, 'normal'))


