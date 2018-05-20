# This program plots the sine function
import turtle, math


coordX = -90
coordY = 90

# x- axis
turtle.speed(8)
turtle.penup()
turtle.goto(-220, 0)
turtle.pendown()

turtle.goto(220, 0)

turtle.degrees()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(220, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

# y-axis

turtle.penup()
turtle.goto(0, -80)
turtle.pendown()

turtle.goto(0, 80)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(240)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(-60)
turtle.forward(20)

turtle.penup()
turtle.goto(-100, -15)
turtle.pendown()
turtle.write("2\u03c0")
turtle.penup()

turtle.goto(-175, 50 * math.sin((-175 / 100) * 2 * math.pi))
turtle.pendown()

for i in range(-175, 176):
    turtle.goto(i, 50 * math.sin((i / 100) * 2 * math.pi))