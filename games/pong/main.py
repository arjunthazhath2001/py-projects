from turtle import Screen
import time


screen= Screen()
screen.bgcolor("black")
screen.title('Pong game')
screen.tracer(0)
screen.setup(width=500, height=500)
screen.listen()



game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)





screen.exitonclick()