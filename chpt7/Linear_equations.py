# This program depicts a  2 by 2 system of linear equations
# It prompts the user to enter the values a , b , c , d , e , and f for the linear equations:f
# x = ed - bf / ad - bc       and  y = af - ec / ad - bc
#
# and  and displays the result. If ad - bc is 0 , it prints the message “The equation has no solution.


class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = c
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def get_ad_minus_bc_constant(self):
        return (self.get_a() * self.get_d()) - (self.get_b() * self.get_c())

    def is_solvable(self):
        if self.get_ad_minus_bc_constant() != 0:
            print("The solution of this equation is:", "x=", format(self.get_x(), ".2f"), "and", "y",
                  format(self.get_y(), ".2f"))
        else:
            print("This equation has no solution")

    def get_x(self):
        return ((self.get_e() * self.get_d()) - (self.get_b() * self.get_f())) / self.get_ad_minus_bc_constant()

    def get_y(self):
        return ((self.get_a() * self.get_f()) - (self.get_e() * self.get_c())) / self.get_ad_minus_bc_constant()


def main():
    a, b, c, d, e, f = eval(input("Enter the values a, b, c, d, e, f for two linear equations where "
                                  "equation1= ax + by = e and equation2= cx + dy = f\n"
                                  " e.g. 1,4,3,7,9,11: "))

    sample1 = LinearEquation(a, b, c, d, e, f)
    sample1.is_solvable()


main()