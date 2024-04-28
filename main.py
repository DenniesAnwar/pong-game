import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(RIGHT_POS)
left_paddle = Paddle(LEFT_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.rally()

    if ball.distance(right_paddle) > 50 and ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()


    if ball.distance(left_paddle) > 50 and ball.xcor() < -405:
        scoreboard.r_point()
        ball.reset()





screen.exitonclick()
