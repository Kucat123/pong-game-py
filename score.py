from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updatescore()
       

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Score: {self.l_score}", align="center", font=("arial", 26, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("arial", 26, "normal"))

    def lef_score(self):
        self.l_score += 1
        self.updatescore()

    def rig_score(self):
        self.r_score += 1
        self.updatescore()
       