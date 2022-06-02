# Ali Jafarbeglou

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
TEXT_COLOR = "white"

SCORE_COLOR = "#"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.penup()
        self.goto(-10, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)