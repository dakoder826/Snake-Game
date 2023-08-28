from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor(209, 117,  183)
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with walls
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.game_over()
        snake.reset()
        # save score in file
        with open("high_score.txt", mode="w") as file:
            file.write(f"{scoreboard.high_score}")

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            snake.reset()
        # save score in file
        with open("high_score.txt", mode="w") as file:
            file.write(f"{scoreboard.high_score}")

screen.exitonclick()
