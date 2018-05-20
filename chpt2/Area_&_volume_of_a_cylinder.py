# This program computes the area and  volume of a cylinder by getting it's radius and
# length from the user

PI = 3.14

radius, length = eval(input("Enter the radius and length of a cylinder: "))


area = radius * radius * PI
volume = area * length

print("The area is: ", area)
print("The volume is: ", volume)

