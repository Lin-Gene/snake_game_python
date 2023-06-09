import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

game_is_on = True
not_quitting = True

while not_quitting:



    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    snek = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(key="Up", fun=snek.face_up)
    screen.onkey(key="Down", fun=snek.face_down)
    screen.onkey(key="Left", fun=snek.face_left)
    screen.onkey(key="Right", fun=snek.face_right)

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snek.snake_move()

        #detect collision with food:
        if snek.head.distance(food) < 15:
            scoreboard.update_score()
            snek.add_segment()
            food.refresh()

        #detect collision with wall
        if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        #detect collision with tail
        for segment in snek.snake_body[1:]:
            if snek.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    continue_game = turtle.textinput("Play again?", "Press Y to play again, or any other input to quit.")

    if continue_game == "y":
        game_is_on = True
        screen.clear()
    else:
        not_quitting = False



screen.exitonclick()