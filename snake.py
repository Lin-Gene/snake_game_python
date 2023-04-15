from turtle import Screen, Turtle



class Snake:
    def __init__(self):
        self.snake_body = []
        self.starting_snake()
        self.head = self.snake_body[0]

    def starting_snake(self):
        position_x = 0
        for num in range(3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(x=position_x, y=0)
            self.snake_body.append(new_square)
            position_x -= 20

    def add_segment(self):
        additional_square = Turtle(shape="square")
        additional_square.color("white")
        additional_square.penup()
        additional_square.goto(self.snake_body[-1].position())
        self.snake_body.append(additional_square)

    def face_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def face_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def face_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def face_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def snake_move(self):
        for ref in range(len(self.snake_body), 0, -1):
            if ref != 1:
                self.snake_body[ref-1].goto(self.snake_body[ref - 2].position())
            elif ref == 1:
                self.snake_body[0].forward(20)


