# This program calculates the area and perimeter of two rectangles of width1 3.5 and height1 35.5 and
# width2 4 and height2 40


class Rectangle:
    def __init__(self, width=1.0, height=2.0):
        self.__width = width
        self.__height = height

    def rectangle_area(self):
        return self.__width * self.__height

    def rectangle_perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


def main():
    rectangle1 = Rectangle(3.5, 35.7)

    rectangle2 = Rectangle(4.0, 40.0)

    print("\nThe Area and Perimeter of two Rectangles\nWidth1:", rectangle1.get_width(), "\t|\tHeight1:",
          rectangle1.get_height(), "\t|\tArea1:", rectangle2.rectangle_area(), "m2", "\t|\tPerimeter1:",
          rectangle2.rectangle_perimeter(), "m", "\nWidth2:", rectangle2.get_width(), "\t|\tHeight2:",
          rectangle2.get_height(), "\t|\tArea1:", rectangle2.rectangle_area(), "m2", "\t|\tPerimeter2:",
          rectangle2.rectangle_perimeter(), "m")


main()