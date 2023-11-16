from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coordinate):
        """Initialize the Paddle object."""
        super().__init__()
        self.penup()
        self.speed(0)
        self.color('white')
        self.shape('square')
        self.shapesize(1, 5)
        self.setheading(90)
        self.goto(x_coordinate, 15)

    def up(self):
        """Move the paddle up if within bounds."""
        if self.ycor() < 230:
            self.setheading(90)
            self.forward(20)

    def down(self):
        """Move the paddle down if within bounds."""
        if self.ycor() > -220:
            self.setheading(270)
            self.forward(20)

    def reset_position(self):
        """Reset the paddle position to the center."""
        self.sety(15)
