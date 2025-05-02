from turtle import Screen,Turtle
import time
from ball import Ball
from midline import Midline
from paddle import Paddle
from score import ScoreBoard


screen= Screen()
screen.bgcolor("black")
screen.title('Pong game')
screen.tracer(0)
screen.setup(width=900, height=600)
screen.listen()

midline=Midline()
ball= Ball()
Lpaddle= Paddle("left")
Rpaddle= Paddle("right")

Lscore= ScoreBoard("left")
Rscore= ScoreBoard("right")

screen.onkey(Lpaddle.moveup,"W")
screen.onkey(Lpaddle.movedown,"A")
screen.onkey(Lpaddle.moveup,"w")
screen.onkey(Lpaddle.movedown,"a")
screen.onkey(Rpaddle.moveup,"Up")
screen.onkey(Rpaddle.movedown,"Down")



game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or  ball.ycor()<-280 :
        ball.ybounce()

    if ball.distance(Rpaddle)<50 or ball.ycor()>280 or ball.distance(Lpaddle)<50 or ball.ycor()<-280:
        ball.xbounce()
    
    if ball.xcor()>550:
        ball.reset()
        Lscore.scoreup()
    
    if ball.xcor()<-550:
        ball.reset()
        Rscore.scoreup()



screen.exitonclick()