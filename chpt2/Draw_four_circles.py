# This program  prompts the user to enter the radius and draws four circles in the center of the screen

import turtle

radius = eval(input("Enter the radius of the circle "))
# Circle 1
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.circle(radius)

turtle.penup()
turtle.goto(radius * 2, 0)
turtle.pendown()

turtle.circle(radius)

turtle.penup()
turtle.goto(0, -radius * 2)
turtle.pendown()

turtle.circle(radius)

turtle.penup()
turtle.goto(radius * 2, -radius * 2)
turtle.pendown()

turtle.circle(radius)


turtle.done()