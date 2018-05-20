# This program  prompts the user to enter  three
# points p1, p2, and p3 for a triangle and display its area below the triangle

import math,turtle, cmath

x1, y1 = eval(input("Enter point one e.g. 4,6 "))
x2, y2 = eval(input("Enter point two e.g. 9,7 "))
x3, y3 = eval(input("Enter point one e.g. 2,8" ))

radius = 6371.01

distance1 = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
distance2 = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
distance3 = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

side = distance1+distance2+distance3

area = math.sqrt(side * (side - distance1) * (side - distance2) * (side - distance3))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("(" + str(x1) + "," + str(y1) + ")")
turtle.goto(x1, y1)
turtle.right(45)
#turtle.forward(distance3)

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.write("(" + str(x2) + "," + str(y2) + ")")
turtle.goto(x2, y2)
turtle.right(90)
#turtle.forward(distance2)

turtle.penup()
turtle.goto(x3, y3)
turtle.pendown()
turtle.write("(" + str(x3) + "," + str(y3) + ")")
turtle.goto(x3, y3)
turtle.right(45)
#turtle.forward(distance3)


turtle.done()
