from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """Initialize the Ball object."""
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(0, 15)
        self.x_move = 4
        self.y_move = 4

    def move(self):
        """Move the ball based on current x and y directions."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Change the y direction to simulate bouncing off the top or bottom."""
        self.y_move *= -1

    def bounce_x(self):
        """
        Change the x direction to simulate bouncing off paddles.
        Increase speed gradually with each bounce.
        """
        self.x_move *= -1
        if self.x_move < 8 and self.y_move < 8:
            self.x_move *= 1.2
            self.y_move *= 1.2

    def reset_position(self):
        """Reset the ball position to the center and change directions."""
        self.goto(0, 15)
        self.x_move *= 4 / self.x_move * -1
        self.y_move *= 4 / self.y_move
