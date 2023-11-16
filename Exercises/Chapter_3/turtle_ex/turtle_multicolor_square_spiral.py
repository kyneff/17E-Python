"""Multi-color squares spirialing outward"""
import turtle
import random

turtle.speed(0)
turtle.pensize(2)
colors = ["turquoise1", "seashell3", "lavender", "magenta2"]
size = 1
while True:
    randomcol = random.choice(colors)
    size += 3
    turtle.pencolor(randomcol)
    turtle.forward(size)
    turtle.left(91)
    turtle.forward(size)
    turtle.left(91)
    turtle.forward(size)
    turtle.left(91)
    turtle.forward(size)
    turtle.left(91)

"""---------------------------------"""