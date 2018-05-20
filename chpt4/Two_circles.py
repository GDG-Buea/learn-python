# This program  prompts the user to enter the center coordinates and radii of two circles and determines whether
# the second circle is inside the first or overlaps with the first

import turtle

x1, y1, radius1 = eval(input("Enter the center of the first circle  and it's radius x1, y1, radius: "))
x2, y2, radius2 = eval(input("Enter the center of the second circle and it's radius x2, y2, radius: "))


# Draw  circle one
turtle.penup()
# Pull the pen up
turtle.goto(x1, y1 - radius1)
turtle.pendown()
# Pull the pen down
turtle.circle(radius1)

turtle.penup()
# Pull the pen up
turtle.goto(x2, y2 - radius2)
turtle.pendown()
# Pull the pen down
turtle.circle(radius2)

# Display the status
turtle.penup()
# Pull the pen up
turtle.goto(x1 - 70, y1 - radius1 - 20)
turtle.pendown()

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5


if d + radius1 <= radius2:
    turtle.write("circle2 is inside circle1")

elif d <= radius2 + radius1:
    turtle.write("circle2 overlaps circle1")
else:
    turtle.write("circle2 does not overlap circle1")


turtle.hideturtle()

turtle.done()
