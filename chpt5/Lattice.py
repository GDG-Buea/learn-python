# This program  displays an 18-by-18 lattice
import turtle

coordX = -90
coordY = 90

turtle.speed(10)
turtle.penup()
turtle.goto(coordX, coordY)
turtle.pendown()

for i in range(1, 20):
    turtle.goto(coordX + 180, coordY)
    turtle.penup()
    coordY -= 10
    turtle.goto(coordX, coordY)
    turtle.pendown()

coordX = -90
coordY = 90

turtle.penup()
turtle.goto(coordX, coordY)
turtle.pendown()

for i in range(1, 20):
    turtle.goto(coordX, coordY - 180)
    turtle.penup()
    coordX += 10
    turtle.goto(coordX, coordY)
    turtle.pendown()

