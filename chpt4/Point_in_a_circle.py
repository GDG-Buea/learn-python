# This program prompts the user to enter a point ( x , y ) and checks whether the point is within the circle
# centered at ( 0 , 0 ) with radius 10 .
# A point is in the circle if its distance to ( 0 , 0 ) is less than or equal to 10 .

x, y = eval(input("Enter a point with two coordinates x, y: "))

distance = ((x ** 2) + (y ** 2)) ** 0.5

if distance <= 10:
    print("Point ", "(", format(x, ".1f"), ",", format(y, ".1f"), ")", " is in the circle")

else:
    print("Point ", "(", format(x, ".1f"), ",", format(y, ".1f"), ")", " is out of the circle")

