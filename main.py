from turtle import Turtle, Screen
import time
import random as rd
from sidepong import Paddle
from balls import Balss
import time
from score import Score
# sidepong = Sidepong()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
balls = Balss()
score = Score()


scren = Screen()
scren.setup(width=800, height=600)
scren.bgcolor("black")
scren.title("pong game")
scren.tracer(0)


scren.listen()
scren.onkey(l_paddle.go_up, "w")
scren.onkey(l_paddle.go_down, "s")

scren.onkey(r_paddle.go_up, "o")
scren.onkey(r_paddle.go_down, "k")

game_on = True
while game_on:
    time.sleep(balls.move_speed)
    scren.update()
    balls.move()

    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce()

    if balls.distance(r_paddle) < 50 and balls.xcor() < 325 or balls.distance(l_paddle) < 50 and balls.xcor() < -325:
        balls.ball_bounce()

    if balls.xcor() > 380:
        balls.reset_poss()
        score.lef_score()
        #game_on = False
    if balls.xcor() < -380:
        balls.reset_poss()
        score.rig_score()
        #score.up_score()








Screen().exitonclick()