from turtle import Turtle, Screen
from paddle import Paddle

# Create Paddle Class
# Create Scoreboard Class
# Create Ball Class

RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(RIGHT_POS)
left_paddle = Paddle(LEFT_POS)


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
