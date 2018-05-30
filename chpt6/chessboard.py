# This program  displays two chessboards side by side
# # Draw one chessboard whose upper-left corner is at

# # (startx, starty) and bottom-right corner is at (endx, endy)
# def drawChessboard(startx, endx, starty, endy):
import turtle


def draw_chessboard(x, y):

    # Draw chess board borders
    turtle.speed(50)
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")

    for i in range(4):
        turtle.forward(240)
        turtle.left(90)

    # Draw chess board inside
    turtle.color("black")
    for j in range(-120, 90, 60):
        for i in range(-120, 120, 60):
            turtle.penup()
            turtle.goto(i, j)
            turtle.pendown()

    # Draw a small rectangle
            turtle.begin_fill()
            for k in range(4):
                turtle.forward(30)
                turtle.left(90)

    for j in range(-90, 120, 60):
        for i in range(-90, 120, 60):
            turtle.penup()
            turtle.goto(i, j)
            turtle.pendown()

    # Draw a small rectangle
            turtle.begin_fill()
            for k in range(4):
                turtle.forward(30)
                turtle.left(90)
            turtle.end_fill()


draw_chessboard(-120, -120)
