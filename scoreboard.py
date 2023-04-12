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
        high_score = 10 # to update with actual score from JSON file (this is for testing purpose only)

        self.setpos(0, 32)
        self.write(arg= "GAME OVER", move= False, align= "center", font= ("Arial", 40, "bold"))
        self.setpos(0, -35)
        self.write(arg=f'Your Score is: {self.curr_score}\nHigh Score is {high_score}', move=False, align="center", font=("Arial", 25, "normal"))