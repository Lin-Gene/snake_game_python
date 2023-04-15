import json
from json.decoder import JSONDecodeError
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.curr_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(x=0, y=280)
        self.print_score()

    def update_score(self):
        self.curr_score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(arg= f"Score: {self.curr_score}", move= False, align = "center", font= ("Arial", 12, "normal"))

    def game_over(self):

        high_score = self.get_high_score()
        self.setpos(0, 32)
        self.write(arg= "GAME OVER", move= False, align= "center", font= ("Arial", 40, "bold"))
        self.setpos(0, -35)
        self.write(arg=f'Your Score is: {self.curr_score}\nHigh Score is {high_score}', move=False, align="center", font=("Arial", 25, "normal"))

    def get_high_score(self):
        with open("highscore.json", "r") as records:
            try:
                score_board = json.load(records)
                if "highScore" in score_board.keys() and score_board["highScore"] >= self.curr_score:
                    return score_board["highScore"]
            except JSONDecodeError:
                pass

        update_score = {
            "highScore": self.curr_score
        }

        with open("highscore.json", "w") as records:
            json.dump(update_score, records)
            return update_score["highScore"]

