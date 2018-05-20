# This program prompts the user to enter the x- and y-coordinates for the three points p0, p1, and p2,
# and displays a message to indicate whether p2 is on the left side, the right side, or on the line from p0 to p1

import turtle

px0, py0 = eval(input("Enter a point with two coordinates x0, y0: "))
px1, py1 = eval(input("Enter a point with two coordinates x1, y1: "))
px2, py2 = eval(input("Enter a point with two coordinates x2, y2: "))

dp2p0 = ((px2 - px0) * (px2 - px0) + (py2 - py0) * (py2 - py0)) ** 0.5
dp2p1 = ((px2 - px1) * (px2 - px1) + (py2 - py1) * (py2 - py1)) ** 0.5

# point 0
turtle.penup()
turtle.goto(px0, py0)
turtle.pendown()
turtle.write("P0 " + str(px0) + "," + str(py0))

# point 1
turtle.penup()
turtle.goto(px0, py0)
turtle.pendown()
turtle.goto(px1, py1)
turtle.write("P0 " + str(px1) + "," + str(py1))
turtle.penup()

# point 2
turtle.goto(px2, py2)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(3)
turtle.end_fill()
turtle.penup()

turtle.goto(px2, py2 - 5)
turtle.pendown()


if dp2p0 > (py0 or px0) and dp2p1 > (py1 or px1):
    turtle.write("P2 is on the right side")

elif dp2p0 < (py0 or px0) and dp2p1 < (py1 or px1):
    turtle.write("P2 is on the left side")

elif dp2p0 == 0 and dp2p1 == 0:
    turtle.write("P2 is on  the line from p0 to p1")
else:
    turtle.write("P2 is out of the line  p0 to p1")


turtle.done()