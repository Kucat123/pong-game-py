from turtle import Turtle

class Balss(Turtle):

    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.shapesize(stretch_wid=1, stretch_len=1)
        # self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        

    def ball_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_poss(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.ball_bounce()
