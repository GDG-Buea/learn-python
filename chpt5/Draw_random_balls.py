# This program displays 10 random balls in a rectangle with width 120 and height 100, centered at (0, 0)

import turtle, random

width = 120
height = 100

# rectangle
turtle.penup()
turtle.goto(-60, -50)
turtle.pendown()
turtle.goto(60, -50)
turtle.goto(60, 50)
turtle.goto(-60, 50)
turtle.goto(-60, -50)

# drawing points
for i in range(1, 11):
    turtle.penup()
    xPos = random.randint(-60, 60)
    yPos = random.randint(-50, 50)
    turtle.goto(xPos, yPos)
    turtle.pendown()
    turtle.dot(2, "green")

turtle.done()