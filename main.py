from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)  # Turn off automatic screen updates

# Create paddles, ball, and scoreboards
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
left_player_scoreboard = Scoreboard(150)
right_player_scoreboard = Scoreboard(-150)

# Listen for keyboard inputs to control the paddles
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)

    ball.move()

    # Bounce off top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Bounce off paddles and update scores
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Reset position and update scores when ball passes paddles
    if ball.xcor() > 380:
        ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()
        right_player_scoreboard.increase_score()

    elif ball.xcor() < -380:
        ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()
        left_player_scoreboard.increase_score()

    # Check for game over conditions
    if left_player_scoreboard.score == 5:
        left_player_scoreboard.game_over('PLAYER 2')
        game_is_on = False
    elif right_player_scoreboard.score == 5:
        right_player_scoreboard.game_over('PLAYER 1')
        game_is_on = False

screen.exitonclick()
