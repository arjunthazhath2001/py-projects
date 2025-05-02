from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time
screen= Screen()
screen.bgcolor("black")
screen.title('Snake game')
screen.tracer(0)
screen.setup(width=500, height=500)
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
        snake.extend()
    
    if (snake.head.xcor()>250 or snake.head.xcor()<-250) or (snake.head.ycor()>250 or snake.head.ycor()<-250):
        score.gameover()
        game_is_on= False

    if len(snake.segments) > 3:
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.gameover()
                game_is_on = False



screen.exitonclick()