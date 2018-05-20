# This program  prompts the user to enter a point (x, y) and checks whether the point is within the rectangle
# centered at ( 0 , 0 ) with width 100 and height 50 .
# It displays the point in the rectangle, and a message indicating whether the point is inside the rectangle

# A point is in the rectangle if its horizontal distance to ( 0 , 0 ) is less than or equal to 10 / 2 and
# its vertical distance to ( 0 , 0 ) is less than or equal to 5.0 / 2 .

import turtle

x, y = eval(input("Enter a point with two coordinates x, y: "))

# rectangle
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.goto(100, 50)
turtle.right(90)
turtle.goto(100, -50)
turtle.right(90)
turtle.goto(100, -50)
turtle.right(90)
turtle.goto(-100, -50)
turtle.right(90)
turtle.goto(-100, 50)

# point
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(3)
turtle.end_fill()
turtle.penup()

turtle.goto(x + 10, y + 10)

if x < (100 // 2) or y < -(50 // 2):
    turtle.write("The point is in the rectangle")

else:
    turtle.write("The point  is out of the rectangle")

turtle.done()