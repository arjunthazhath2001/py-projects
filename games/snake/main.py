from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time
screen= Screen()
screen.bgcolor("black")
screen.title('Snake game')
screen.tracer(0)

screen.listen()

snake= Snake()
food= Food()
score= ScoreBoard()



screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")



game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        score.scoreup()










screen.exitonclick()