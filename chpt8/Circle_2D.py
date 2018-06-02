# This program prompts the user to enter two circles with x- and y-coordinates and the radius,
#  creates two circles and , displays their areas and perimeters, and indicates if the circles overlap,
# or if one is found in another.
#
import math


class Circle2D:
    def __init__(self, x=0.0, y=0.0, radius=0.0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_radius(self):
        return self.__radius

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * pow(self.__radius, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def contains_point(self, x, y):
        d = self.distance(x, y, self.__x, self.__y)
        return d <= self.__radius

    def contains(self, circle):
        d = self.distance(self.__x, self.__y, circle.__x, circle.__y)
        return d + circle.__radius <= self.__radius

    def overlaps(self, circle):
        return self.distance(self.__x, self.__y, circle.__x, circle.__y) <= self.__radius + circle.__radius

    def __contains__(self, another_circle):
        return self.contains(another_circle)

    def __lt__(self, second_circle):
        return self.__cmp__(second_circle) < 0

    def __le__(self, second_circle):
        return self.__cmp__(second_circle) <= 0

    def __gt__(self, second_circle):
        return self.__cmp__(second_circle) > 0

    def __ge__(self, second_circle):
        return self.__cmp__(second_circle) >= 0

        # Compare two numbers
    def __cmp__(self, secondCircle):
        if self.__radius > secondCircle.__radius:
            return 1
        elif self.__radius < secondCircle.__radius:
            return -1
        else:
            return 0

    def distance(self,x1, y1, x2, y2):
        return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def main():

    x1, y1, r1 = eval(input("Enter x1, y1, radius1: "))
    x2, y2, r2 = eval(input("Enter x2, y2, radius2: "))

    c1 = Circle2D(x1, y1, r1)
    c2 = Circle2D(x2, y2, r2)

    print(" Circle One:\n\tArea= ", format(c1.get_area(), ".4f"), "m2\n\tPerimeter= ", format(c1.get_perimeter(), ".4f"),
          "m2\n\nCircle Two:\n\tArea= ", format(c2.get_area(), ".4f"), "m2" "\n\tPerimeter= ",
          format(c2.get_perimeter(), ".4f"), "m2")
    print()

    print("Circle one contains the center of circle two? ", c1.contains_point(c2.get_x(), c2.get_y()), "\n")

    print("Circle one  contains circle two?", c1.contains(c2), "\n")
    print("Circle one  overlaps circle two?", c1.overlaps(c2), "\n")




main()