# This program is based on Quadratic equations
# It prompts the user to enter values for a, b, and c and displays the result
# based on the discriminant.
# If the discriminant is positive, it displays the two roots.
#  If the discriminant is 0 , it displays one root.
# Otherwise, it displays  the message - The equation has no roots
import math


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__var1 = a
        self.__var2 = b
        self.__var3 = c

    def get_a(self):
        return self.__var1

    def get_b(self):
        return self.__var2

    def get_c(self):
        return self.__var3

    def set_a(self, value_a):
        self.__var1 = value_a

    def set_b(self, value_b):
        self.__var2 = value_b

    def set_c(self, value_c):
        self.__var3 = value_c

    def calculate_discriminant(self):
        return (self.__var2 ** 2) - (4 * self.__var1 * self.__var3)

    def get_root1(self):
        return ((-self.__var2) + math.sqrt(self.calculate_discriminant())) / 2 * self.get_a()

    def get_root2(self):
        return ((-self.__var2) - math.sqrt(self.calculate_discriminant())) / 2 * self.get_a()

    def get_roots(self):

        if self.calculate_discriminant() > 0:
            print("The roots of this equation are: ", format(self.get_root1(), ".2f"), "and",
                  format(self.get_root2(), ".2f"))

        elif self.calculate_discriminant() == 0:
                if self.get_root1() != 0:
                    print("The root of this equation is: ", format(self.get_root1(), ".2f"))
                else:
                    print("The root of this equation is: ", format(self.get_root2(), ".2f"))
        else:
                print("This equation has no real roots")


def main():
    value_of_a, value_of_b, value_of_c = eval(input("Enter the values for a, b and c of the quadratic equation "
                                                    "e.g. 3, 4, 5: "))

    user1 = QuadraticEquation(value_of_a, value_of_b, value_of_c)
    user1.get_roots()



main()