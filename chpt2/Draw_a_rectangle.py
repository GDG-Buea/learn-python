# This program prompts the user to enter the center of a rectangle, width, and height, and displays the rectangle

import turtle

center, width, height = eval(input("Enter the center, width and height of a rectangle e.g 5,10,20 "))

turtle.penup()
turtle.goto(center, center/2)
turtle.pendown()

turtle.forward(width)
turtle.right(90)

turtle.forward(height)
turtle.right(90)

turtle.forward(width)
turtle.right(90)

turtle.forward(height)
turtle.right(90)

turtle.done()