from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self, x_coordinate):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x_coordinate, 210)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"GAME OVER! {player} WON!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
