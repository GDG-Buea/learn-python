# This program displays the  speed ,radius , color , and on properties of two fans


SLOW = 1
MEDIUM = 2
FAST = 3


class Fan:
    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = False

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_is_on(self):
        return self.__on

    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_is_on(self, on):
        self.__on = on


def main():
    fan1 = Fan(FAST, 10, 'yellow', True)
    fan2 = Fan(MEDIUM, 5, 'blue', False)

    print()
    print("Fan one has the following properties: ", "Speed=", fan1.get_speed(), "\t|\tColor=", fan1.get_color(),
          "\t|\tStatus= ", fan1.get_is_on())
    print()
    print("Fan two has the following properties: ", "Speed=", fan2.get_speed(), "\t|\tColor=", fan2.get_color(),
          "\t|\tStatus= ", fan2.get_is_on())
    print()


main()