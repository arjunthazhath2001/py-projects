from turtle import Turtle,Screen
from snake import Snake
import time
screen= Screen()
screen.bgcolor("black")
screen.title('Snake game')
screen.tracer(0)


snake= Snake()



game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()









screen.exitonclick()