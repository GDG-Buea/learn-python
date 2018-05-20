# This program prompts the user to enter the length from the center of a pentagon to a vertex and
#  computes the area of the pentagon.

import math, turtle

r = eval(input("Enter the length from the center to a vertex: "))
s = 2 * r * math.sin(math.pi/5)
area = 3 * math.sqrt(3) / 2 * pow(s, 2)

print("The area of the pentagon is: ", format(area, ".2f"))

