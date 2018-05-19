# This  program  prompts the user to enter the length of the star and draws it star,

import turtle

length = eval(input("Enter the length of the star: "))

turtle.penup()
turtle.goto(-length, -length)
turtle.pendown()

turtle.right(216)
turtle.forward(length)

turtle.right(144)
turtle.forward(length + length // 10)

turtle.right(144)
turtle.forward(length)

turtle.right(144)
turtle.forward(length)

turtle.setheading(0)
turtle.right(78)
turtle.forward(length)

turtle.done()
