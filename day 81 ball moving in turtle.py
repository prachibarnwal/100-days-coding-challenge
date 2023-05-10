import turtle
import time
import random

def moveleft():
    xb = ball.xcor()
    ball.setx(xb-10)

def moveright():
    xb = ball.xcor()
    ball.setx(xb+10)

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

wn.listen()
wn.onkeypress(moveleft,'l')
wn.onkeypress(moveright,'r')
wn.onkeypress(moveup,'u')
wn.onkeypress(movedown,'d')

while True:
    wn.update()
    
