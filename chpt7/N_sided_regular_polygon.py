# This program displays the perimeter and area of three regular polygons
#
# An n-sided regular polygon’s sides all have the same length and all of its angles have the same degree
# (i.e., the polygon is both equilateral and equiangular).


import math


class RegularPolygon:
    def __init__(self, n=3, side=3, x=0.0, y=0.0):
        self.__var1 = n
        self.__var2 = side
        self.__var3 = x
        self.__var4 = y

    def get_number_of_sides(self):
        return self.__var1

    def get_length_of_side(self):
        return self.__var2

    def get_x_center_axis(self):
        return self.__var3

    def get_y__center_axis(self):
        return self.__var4

    def set_number_of_sides(self, number_of_sides):
        self.__var1 = number_of_sides

    def set_length_of_side(self, length_of_side):
        self.__var2 = length_of_side

    def set_x_center_axis(self, x_axis):
        self.__var3 = x_axis

    def set_y__center_axis(self, y_axis):
        self.__var4 = y_axis

    def regular_polygon_area(self):
        return (self.__var1 * pow(self.__var2, 2)) / 4 * math.tan(math.pi / self.__var1)

    def regular_polygon_perimeter(self):
        return self.__var1 * self.__var2


def main():

    hexagon = RegularPolygon(6, 4)
    decagon = RegularPolygon(10, 4, 5.6, 7.8)

    print()
    print("__________________________________________________________________________________________")
    print()

    print("Polygon one:\tnumber of sides=", hexagon.get_number_of_sides(), "\t\tlength of side=",
          hexagon.get_length_of_side())
    print("\n\t\t\t\tArea=", format(hexagon.regular_polygon_area(), ".2f"), "m2", "\t\t\tPerimeter=",
          format(hexagon.regular_polygon_perimeter(), ".2f"), "m")
    print()
    print("__________________________________________________________________________________________")
    print()

    print("Polygon two;\tnumber of sides=", decagon.get_number_of_sides(), "\tlength of side=",
          decagon.get_length_of_side())
    print("\n\t\t\t\tArea=", format(decagon.regular_polygon_area(), ".2f"), "m2", "\t\t\tPerimeter=",
          format(decagon.regular_polygon_perimeter(), ".2f"), "m")
    print()
    print("__________________________________________________________________________________________")



main()