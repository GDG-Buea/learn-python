# The great circle distance is the distance between
# two points on the surface of a sphere. Let (x1, y1) and (x2, y2) be the geographical
# latitude and longitude of two points. The great circle distance between the two
# points can be computed using the following formula:
# d = radius * arccos(sin(x 1 ) * sin(x 2 ) + cos(x 1 ) * cos(x 2 ) * cos(y 1 - y 2 ))
# ___________________________________________________________________________________________________________
# This program  prompts the user to enter the latitude and longitude of two points on the earth in degrees
# and displays its great circle distance.

import math , cmath

x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)

averageRadiusOfEarth = 6371.01
A = math.sin(x1) * math.sin(x2)
B = math.cos(x1) * math.cos(x2)
C = math.cos(y1 - y2)

greatCircleDistance = averageRadiusOfEarth * math.acos(A + B * C)

# 41.5,87.37
print("The distance between the two points is: ", greatCircleDistance, "Km")
