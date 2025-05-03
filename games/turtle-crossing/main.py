from turtle import Screen
import time
from animal import Animal
from cars import Car
from score import ScoreBoard

screen= Screen()

screen.title('Turtle crossing game')
screen.tracer(0)
screen.setup(width=500, height=500)
screen.listen()


animal= Animal()
car= Car()
score= ScoreBoard()

screen.onkey(animal.move,"Up")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    
    car.create_car()
    car.move()
    
    if animal.ycor()>220:
        animal.goto(0,-200)
        score.scoreup()
        car.refresh()
        
    for c in car.segments:
        if c.distance(animal)<20:
            game_is_on= False
            score.gameover()


screen.exitonclick()