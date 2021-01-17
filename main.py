from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.score_check()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameState = 1
while gameState:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.point()
        snake.extend()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor())  > 280:
        gameState = False
        scoreboard.game_over()

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameState = False
            scoreboard.game_over()

screen.exitonclick()
