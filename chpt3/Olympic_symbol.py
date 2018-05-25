# This program prompts the user to enter the radius of the rings and draws an Olympic symbol of five rings of the
# same size with the colors blue, black, red, yellow, and green,

import turtle

radius = eval(input("Enter the radius of the circle: "))


#Blue circle
turtle.penup()
turtle.goto(-radius, radius)
turtle.pendown()


turtle.color('blue')
turtle.speed(9)
turtle.circle(radius)

#Black circle
turtle.penup()
turtle.speed(9)
turtle.forward(radius * 3)
turtle.pendown()

turtle.color('black')
turtle.speed(9)
turtle.circle(radius)

#Red circle
turtle.penup()
turtle.speed(9)
turtle.forward(radius * 3)
turtle.pendown()

turtle.color('red')
turtle.speed(9)
turtle.circle(radius)

#Yellow circle
turtle.penup()
turtle.goto(-radius, -radius / 8)
turtle.speed(9)
turtle.pendown()


turtle.penup()
turtle.speed(9)
turtle.forward(radius * 1.5)
turtle.pendown()

turtle.color('yellow')
turtle.speed(9)
turtle.circle(radius)

#Green Circle
turtle.penup()
turtle.speed(9)
turtle.forward(radius * 3)
turtle.pendown()


turtle.color('green')
turtle.speed(9)
turtle.circle(radius)

turtle.done()
