from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 50, "bold")
GAME_OVER_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self, x_coordinate):
        """Initialize the Scoreboard object."""
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x_coordinate, 210)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the displayed score on the screen."""
        self.write(f"{self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self, player):
        """Display game over message with the winning player."""
        self.goto(0, 0)
        self.write(f"GAME OVER! {player} WON!", align=ALIGNMENT, font=GAME_OVER_FONT)

    def increase_score(self):
        """Increase the score and update the scoreboard."""
        self.score += 1
        self.clear()
        self.update_scoreboard()
