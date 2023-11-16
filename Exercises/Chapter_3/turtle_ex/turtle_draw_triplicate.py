import turtle
import numpy as np
import random

#How many times to do you want this program to repeat?
howmanyturtles = int (input("How mant Turtle runs do you want? "))

#Triangle function. By tweaking these variables, you may create different shapes to be drawn.
def drawtriangle():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)

    turtle.forward(150)
    turtle.left(240)
    turtle.forward(150)
    turtle.left(240)
    turtle.forward(150)
    turtle.left(240)

    turtle.forward(200)
    turtle.left(480)
    turtle.forward(200)
    turtle.left(480)
    turtle.forward(200)
    turtle.left(480)

#Turning function.
def turnhop():
    turtle.left(np.pi*2.2)
    turtle.forward(30)

#Bounce out and back funcitons.
def bounce():
    turtle.forward(10)

#Color selection and pensize functions.
color = ("maroon", "thistle", "goldenrod", "hot pink", "dim gray", "sky blue", "medium purple")
def randcolor():
    turtle.pencolor(random.choice(color))
    turtle.pensize(4)

#Speed is constant, but can be changed to either speed up or slow down the drawing process beforehand.
#Speeds are 1 (slowest) through 10 (fastest.)
#The following commands are where all the previously defined functions are performed at speed:
#randcolor, drawtriangle, turnhop, bounce

turtle.speed(5)
for i in range(howmanyturtles):
    randcolor()
    drawtriangle()
    turnhop()
    bounce()

#Leave the following line as is, so that the generated image stays open when program completes.
turtle.mainloop()