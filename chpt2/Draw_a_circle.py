# This program  prompts a user to enter the center and radius of a circle, and then displays the circle and its area

import turtle

center, radius = eval(input("Enter the center and radius of a circle you desire: "))

PI = 3.14

area = PI * radius ** 2

turtle.penup()
turtle.goto(center, center)
turtle.pendown()

turtle.circle(radius)

turtle.penup()
turtle.goto(center, center * 10)
turtle.pendown()

turtle.write(area)

turtle.done()