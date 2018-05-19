# This program  displays a STOP sign, i.e. The hexagon is in red and the text is in white.

import turtle

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(90, steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(-70, -40)
turtle.pendown()
turtle.color('white')
turtle.write("STOP", font=("Arial ", 38, "bold"))


turtle.done()
