# This program  draws four hexagons in the center of the screen

import turtle

side = eval(input("Enter the side of the hexagon "))
gap = 2
# Hexagon 1
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(90)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)


# Hexagon 2
turtle.penup()
turtle.goto(side * 2 + gap, 0)
turtle.right(90)
turtle.pendown()

turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(90)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)


# Hexagon 3

turtle.penup()
turtle.goto(0, - (side * (2.4)))
turtle.pendown()

turtle.right(90)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(90)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

# Hexagon 4

turtle.penup()
turtle.goto(side * 2 + gap, - (side * 2.4))
turtle.pendown()

turtle.right(90)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(90)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)

turtle.right(45)
turtle.forward(side)


turtle.done()