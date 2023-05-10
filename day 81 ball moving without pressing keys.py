import turtle
import time
import random

def moveup():
    y = ball.ycor()
    ball.sety(y+10)

def movedown():
    y = ball.ycor()
    ball.sety(y-10)
    
wn = turtle.Screen()
wn.title("Bouncing Ball Game")
wn.bgcolor("cyan")
wn.setup(width = 600, height = 600)

ball = turtle.Turtle()

ball.color("RED")
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid = 6, stretch_len = 6)
ball.penup()

h = 0

while True:
    if h ==0:
        moveup()
    if h == 1:
        movedown()

    if ball.ycor() >=300:
        h = 1
    if ball.ycor() <= -300:
        h = 0
    time.sleep(0.1)
    wn.update()
    
