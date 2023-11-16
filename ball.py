from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(0, 15)
        self.x_move = 4
        self.y_move = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.x_move < 8 and self.y_move < 8:
            self.x_move *= 1.2
            self.y_move *= 1.2

    def reset_position(self):
        self.goto(0, 15)
        self.x_move *= 4 / self.x_move * -1
        self.y_move *= 4 / self.y_move
