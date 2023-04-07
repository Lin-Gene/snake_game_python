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
        self.write(arg= f"Score: {self.curr_score}", move= False, align = "center", font= ("Arial", 11, "normal"))

    def game_over(self):
        self.setpos(0,0)
        self.write(arg= "GAME OVER", move= False, align= "center", font= ("Arial", 30, "normal"))
