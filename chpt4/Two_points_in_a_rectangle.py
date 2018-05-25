# This program prompts the user to enter a point (x, y) and checks whether the point is within the rectangle
# centered at ( 0 ,0 ) with width 100 and height 50 . It displays the point, the rectangle, and a message
# indicating whether the point is inside the rectangle in the window, a

import turtle

x1, y1 = eval(input("Enter a point x,y: "))
width = 100
height = 50


turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(3)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)

turtle.penup()
turtle.goto(200, -150)
turtle.pendown()

d = ((0 - x1) * (0 - x1) + (0 - y1) * (0 - y1)) ** 0.5

if d < width or height:
    print("The dot is inside the circle")
else:
    print("The dot is out of the circle")


turtle.done()