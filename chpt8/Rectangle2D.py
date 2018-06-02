
# This program prompts the user to enter two rectangles with center x-, y-coordinates,width, and height,
#  creates two rectangles, displays their areas and perimeters, and displays a the truth value of
#  rectangle containing the center of rectangle2, rectangle contains rectangle2, rectangle overlapping rectangle2,

import math


class Rectangle2D:

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Boundaries of Rectangle
        self.left_boundary = self.x - (self.width / 2)
        self.right_boundary = self.x + (self.width / 2)
        self.up_boundary = self.y + (self.height / 2)
        self.down_boundary = self.y - (self.height / 2)

        # Intervals
        self.x_interval = [self.left_boundary, self.right_boundary]
        self.y_interval = [self.down_boundary, self.up_boundary]

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def contains_point(self, point_x, point_y):
        y_aligned = False
        x_aligned = False

        # Aligned on x axis?
        if self.right_boundary <= point_x >= self.left_boundary :
            x_aligned = True

        # Aligned on y axis?
        if self.up_boundary <= point_y >= self.down_boundary:
            y_aligned = True

        if y_aligned and x_aligned:
            return True
        else:
            return False

    def contains(self, rectangle2d):
        x1 = self.x_interval
        x2 = rectangle2d.x_interval
        y1 = self.y_interval
        y2 = rectangle2d.y_interval

        x_interception = False
        y_interception = False

        # Is either end within the other rectangle?
        if (x1[1] < x2[0] > x1[0]) or (x1[1] < x2[1] > x1[0]):
            x_interception = True
        else:
            x_interception = False

        if (y1[1] < y2[0] > y1[0]) or (y1[1] < y2[1] > y1[0]):
            y_interception = True
        else:
            y_interception = False

        if x_interception and y_interception:
            return True
        else:
            return False

    def overlaps(self, rectangle2d):
        if (self.left_boundary < rectangle2d.right_boundary and self.right_boundary > rectangle2d.left_boundary
                and self.down_boundary < rectangle2d.up_boundary and self.up_boundary > rectangle2d.down_boundary):
            return True
        else:
            return False

    def __contains__(self, another):
        return self.contains(another)

    def __cmp__(self, other):
        if self.get_area() < other.getArea():
            return -1
        elif self.get_area() == other.getArea():
            return 0
        elif self.get_area() > other.getArea():
            return 1

    def __lt__(self, other):
        return self.get_area() < other.getArea()

    def __le__(self, other):
        return self.get_area() <= other.getArea()

    def __eq__(self, other):
        return self.get_area() == other.getArea()

    def __ne__(self, other):
        return self.get_area() != other.getArea()

    def __gt__(self, other):
        return self.get_area() > other.getArea()

    def __ge__(self, other):
        return self.get_area() >= other.getArea()


def main():
    r1 = Rectangle2D(*[float(i) for i in input('Enter x1, y1, width1, height1: ').split(',')])
    r2 = Rectangle2D(*[float(i) for i in input('Enter x2, y2, width2, height2: ').split(',')])

    print("Rectangle One\n\tArea= ", r1.get_area(), "m2\n\tPerimeter= ", r1.get_perimeter(), "m2")
    print("Rectangle Two\n\tArea= ", r2.get_area(), "m2\n\tPerimeter= ", r2.get_perimeter(), "m2")
    print("Rectangle One contains the center of Rectangle Two? ", r1.contains_point(r2.get_x(), r2.get_y()))
    print("Rectangle One contains Rectangle Two? ", r1.contains(r2))
    print("Rectangle One overlaps Rectangle Two? ", r1.overlaps(r2))


main()
