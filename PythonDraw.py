import turtle
from turtle import *
import turtle as t
turtle.setup(650,350,200,200) # location of window
# turtle.goto() go straight
# turtle.fd() go ahead
# turtle.bk() go back
# turtle.circle() go twist
# turtle,seth() set angle
# turtle.left() go left
# turtle.right() go right
# RGB red green blue (0-255)
# turtle.colormode(mode) mode ? 1.0 small : 255 integer
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
# turtle.penup() start to draw
# turtle.pendown() stop to draw
# turtle.pensize() set size
# range(N) generate N numbers
# range(M,N) generate numbers from M to N
for i in range(4):
# turtle.circle(r,extent=None) According radis to change arch
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
# turtle.done() do not exit immediately
