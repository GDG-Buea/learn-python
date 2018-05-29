# This program reads three sides for a triangle and computes the area if the input is valid, otherwise,
#  it displays that the input is invalid.

import cmath


def area(side1, side2, side3):

    s = (side1 + side2 + side3) / 2

    triangle_area = cmath.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    return format(abs(triangle_area), ".2f")


def is_valid(s1, s2, s3):
    if (s1 > s2 + s3) or (s2 > s1 + s3) or (s3 > s1 + s2):

        return "The area is " + area(s1, s2, s3) + "m2"
    else:
        return 'Input is invalid'


def main():
    side_one, side_two, side_three = eval(input("Enter the three sides of a triangle: "))
    print(is_valid(side_one, side_two, side_three))


main()

