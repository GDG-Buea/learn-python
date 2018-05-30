# This program fills a rectangle with the specified color, width, and height, and a circle with the specified
# color, center, and radius.

import turtle
import random
import math


def draw_rectangle(color="black", width=30, height=30):

    # rectangle
    turtle.penup()
    turtle.color(color)
    turtle.goto(-width, -height)
    turtle.pendown()
    turtle.goto(width, -height)
    turtle.goto(width, height)
    turtle.goto(-width, height)
    turtle.goto(-width, -height)

    random_points(width, height)


def random_points(width, height):

    # drawing points
    for i in range(1, 11):
        turtle.penup()

        x_pos = random.randint(-width, width)
        y_pos = random.randint(-height, height)
        turtle.goto(x_pos, y_pos)
        turtle.pendown()
        turtle.dot(2, "green")


# Draw  circle
def draw_circle(color="green", x=100, y=-200, radius=50):

    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

    random_points(radius, radius)


def main():
    draw_rectangle()
    draw_circle()
    turtle.done()


main()
