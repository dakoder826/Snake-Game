from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = "Times New Roman", 17, "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(1, 4, 2)
        self.penup()
        self.setposition(-50, 270)
        with open("high_score.txt") as file:
            self.contents = file.read()
        self.high_score = int(self.contents)
        self.update_score()
        self.game_ended = False

    def update_score(self):
        self.clear()
        self.setposition(0, 270)
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
           self.high_score = self.score
        self.score = 0
        time.sleep(0.5)
        self.update_score()
        time.sleep(0.5)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()








