# This  program  prompts the user to enter the center x-, y-coordinates, width, and height of two rectangles and determines
# whether the second rectangle is inside the first or overlaps with the first

import turtle

x1, y1 = eval(input("Enter the center of the first rectangle  x1, y1: "))
width1, height1 = eval(input("Enter the width and height of the first rectangle  width1, height1: "))
x2, y2 = eval(input("Enter the center of the second rectangle x2, y2: "))
width2, height2 = eval(input("Enter the width and height of the first rectangle  width2, height2: "))

# rectangle 1
turtle.penup()
turtle.goto(height1, width1)
turtle.pendown()
turtle.right(90)
turtle.goto(height1, -width1)
turtle.right(90)
turtle.goto(height1, -width1)
turtle.right(90)
turtle.goto(-height1, -width1)
turtle.right(90)
turtle.goto(-height1, width1)
turtle.right(90)
turtle.goto(height1, width1)


# rectangle 2
turtle.penup()
turtle.goto(height2, width2)
turtle.pendown()
turtle.goto(height2, width2)
turtle.right(90)
turtle.goto(height2, -width2)
turtle.right(90)
turtle.goto(height2, -width2)
turtle.right(90)
turtle.goto(-height2, -width2)
turtle.right(90)
turtle.goto(-height2, width2)
turtle.right(90)
turtle.goto(-height2, width2)
turtle.right(90)
turtle.goto(height2, width2)

# Display the status
turtle.penup()
# Pull the pen up
turtle.goto(x1 - 70, y1 - height1 - 20)
turtle.pendown()

if (int((y2 - y1 ** 2) ** 0.5) + height2 // 2 <= height1 // 2) and \
        (int((x2 - x1 ** 2) ** 0.5) + width2 // 2 <= width1 // 2) and\
        (height1 // 2 + height2 // 2) <= height1 and (width1 // 2 + width2 // 2) <= width1:
    print("r2 is inside r1")

elif (x1 + width1 // 2 > x2 - width2) or (y1 + height1 // 2 > y2 - height2):
    print("r2 overlaps r1")
else:
    print("r2 doe not overlap r1")



turtle.done()

# w2 = w2 / 2;
# h2 = h2 / 2;
#
# // Calculating
# range
# of
# r1 and r2
# double
# x1max = x1 + w1;
# double
# y1max = y1 + h1;
# double
# x1min = x1 - w1;
# double
# y1min = y1 - h1;
# double
# x2max = x2 + w2;
# double
# y2max = y2 + h2;
# double
# x2min = x2 - w2;
# double
# y2min = y2 - h2;
#
# if (x1max == x2max & & x1min == x2min & & y1max == y2max
#         & & y1min == y2min) {
# // Check if the two are identicle
# System.out.print("r1 and r2 are indentical");
#
# } else if (x1max <= x2max & & x1min >= x2min & & y1max <= y2max
# & & y1min >= y2min) {
# // Check if r1 is in r2
# System.out.print("r1 is inside r2");
# } else if (x2max <= x1max & & x2min >= x1min & & y2max <= y1max
# & & y2min >= y1min) {
# // Check if r2 is in r1
# System.out.print("r2 is inside r1");
# } else if (x1max < x2min | | x1min > x2max | | y1max < y2min
# | | y2min > y1max) {
# // Check if the two overlap
# System.out.print("r2 does not overlaps r1");
# } else {
# System.out.print("r2 overlaps r1");