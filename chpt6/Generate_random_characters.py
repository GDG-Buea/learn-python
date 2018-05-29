# This program displays 100 lowercase letters, fifteen per line

import turtle
from random import randint


def get_random_lower_case_letter():
    return get_random_character('a', 'z')


def get_random_character(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def write_text(s, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write(s)
        turtle.goto(x, y)
        turtle.done()


def main():
    count = 0
    number_of_characters = 100
    characters_per_line = 15
    print("\n")

    for i in range(number_of_characters):
        print("\t", get_random_lower_case_letter(),  end=' ')
        count += 1

        if count % characters_per_line == 0:
            print()


main()

print()

# Draw a line from (x1, y1) to (x2, y2)
# def drawLine(x1, y1, x2, y2):
# turtle.penup()
# turtle.goto(x1, y1)
# turtle.pendown()
# turtle.goto(x2, y2)


# def writeText(s, x, y):
# turtle.penup() # Pull the pen up
# turtle.goto(x, y)
# turtle.pendown() # Pull the pen down
# turtle.write(s) # Write a string

# # Draw a point at the specified location (x, y)
# def drawPoint(x, y):
# turtle.penup() # Pull the pen up
# turtle.goto(x, y)
# turtle.pendown() # Pull the pen down
# turtle.begin_fill() # Begin to fill color in a shape
# turtle.circle(3)
# turtle.end_fill() # Fill the shape


# # Draw a circle centered at (x, y) with the specified radius
# def drawCircle(x = 0, y = 0, radius = 10):
# turtle.penup() # Pull the pen up
# turtle.goto(x, y - radius)
# turtle.pendown() # Pull the pen down
# turtle.circle(radius)


# # Draw a rectangle at (x, y) with the specified width and height
# def drawRectangle(x = 0, y = 0, width = 10, height = 10):
# turtle.penup() # Pull the pen up
# turtle.goto(x + width / 2, y + height / 2)
# turtle.pendown() # Pull the pen down
# turtle.right(90)
# turtle.forward(height)
# turtle.right(90)
# turtle.forward(width)
# turtle.right(90)
# turtle.forward(height)
# turtle.right(90)
# turtle.forward(width)

# Generate a random uppercase letter
# def getRandomUpperCaseLetter() :
# return getRandomCharacter('A', 'Z')

# # Generate a random digit character
# def getRandomDigitCharacter() :
# return getRandomCharacter('0', '9')

# # Generate a random character
# def getRandomASCIICharacter() :
# return chr(randint(0, 127))
#
# # Generate a random character between ch1 and ch2
# def getRandomCharacter(ch1, ch2) :
# return chr(randint(ord(ch1), ord(ch2)))
#


