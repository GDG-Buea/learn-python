# This program prints a table with three columns and five rows

import turtle

# Colummn one
turtle.color("black")
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.write("a")

turtle.penup()
turtle.goto(-200, 180)
turtle.pendown()
turtle.write("1")

turtle.penup()
turtle.goto(-200, 160)
turtle.pendown()
turtle.write("2")

turtle.penup()
turtle.goto(-200, 140)
turtle.pendown()
turtle.write("3")

turtle.penup()
turtle.goto(-200, 120)
turtle.pendown()
turtle.write("4")

#Column two
turtle.penup()
turtle.goto(-120, 200)
turtle.pendown()
turtle.write("a^2")

turtle.penup()
turtle.goto(-120, 180)
turtle.pendown()
turtle.write("1")

turtle.penup()
turtle.goto(-120, 160)
turtle.pendown()
turtle.write("4")

turtle.penup()
turtle.goto(-120, 140)
turtle.pendown()
turtle.write("9")

turtle.penup()
turtle.goto(-120, 120)
turtle.pendown()
turtle.write("16")



#Column three
turtle.penup()
turtle.goto(-40, 200)
turtle.pendown()
turtle.write("a^3")

turtle.penup()
turtle.goto(-40, 180)
turtle.pendown()
turtle.write("1")

turtle.penup()
turtle.goto(-40, 160)
turtle.pendown()
turtle.write("8")

turtle.penup()
turtle.goto(-40, 140)
turtle.pendown()
turtle.write("27")

turtle.penup()
turtle.goto(-40, 120)
turtle.pendown()
turtle.write("64")



turtle.done()