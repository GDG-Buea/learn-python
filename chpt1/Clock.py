#(Turtle: display a clock) This program  displays a clock that shows the time 9:15:00

import turtle

turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.circle(180)

# Number 12
turtle.penup()
turtle.goto(-10, 200)
turtle.goto(-10, 180)
turtle.pendown()
turtle.write("12")

# Number 6
turtle.penup()
turtle.goto(-10, -200)
turtle.goto(-10, -140)
turtle.pendown()
turtle.write("6")

#  Number 9
turtle.penup()
turtle.goto(-180, 20)
turtle.goto(-160, 20)
turtle.pendown()
turtle.write("9")

# Number 3

turtle.penup()
turtle.goto(180, 20)
turtle.goto(160, 20)
turtle.pendown()
turtle.write("3")

# Time
turtle.penup()
turtle.goto(-40, -180)
turtle.pendown()
turtle.write("9:15:00 AM")

# minute hand
turtle.penup()
turtle.goto(0, 25)
turtle.goto(0, 25)
turtle.pendown()
turtle.forward(150)

#hour hand
turtle.penup()
turtle.goto(0, 25)
turtle.goto(0, 25)
turtle.pendown()
turtle.right(180)
turtle.forward(75)
turtle.penup()
turtle.goto(-80, 30)
turtle.pendown()
turtle.circle(5)

# O'clock hand
turtle.penup()
turtle.goto(-7, 25)
turtle.goto(-7, 25)
turtle.pendown()
turtle.right(90)
turtle.forward(150)

turtle.done()