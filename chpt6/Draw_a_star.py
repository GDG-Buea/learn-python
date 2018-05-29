# This program  draws a star

import turtle


def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.done


def turn_angle(n):
    turtle.right(n)


def main():
    drawLine(-80, 0, 80, 0)
    turn_angle(144)

    drawLine(80, 0, 0, -80)
    turn_angle(144)

    drawLine(0, -80, 0, 80)
    turn_angle(144)

    drawLine(0, 80, 60, -80)
    turn_angle(144)
    drawLine(60, -80, -80, 0)

    turtle.done()


main()






#
# star = turtle.Turtle()
#
# for i in range(50):
#     star.forward(50)
#     star.right(144)
#
# turtle.done()