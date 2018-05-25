#  The two roots of a quadratic equation, for example, ax 2 + bx + c = 0, can be obtained using the formula:
# r1= (-b + (b*b - 4ac)^0.5)/2a  and  r2= (-b - (b*b - 4ac)^0.5)/2a
#
# b*b - 4ac is called the discriminant of the quadratic equation.
#
# If it is positive, the equation has two real roots.
# If it is zero, the equation has one root.
# If it is negative,the equation has no real roots.

# This program prompts the user to enter values for a, b, and c and displays the result based on the discriminant.
# If the discriminant is positive,it displays two roots.
# If the discriminant is 0 , it displays one root, otherwise, it displays the message - The equation has no real roots


a, b, c = eval(input("Enter the values of a, b and c of the quadratic equation e.g 2,4,8 "))

discriminant = b * b - 4 * a * c

root1 = (- b + (discriminant ** 0.5)) / (2 * a)
root2 = (- b - (discriminant ** 0.5)) / (2 * a)

if discriminant > 0:
    print("The roots are ", format(root1, ".4f"), "and", format(root2, ".4f"))

elif discriminant == 0:
    print("The root is ", round(root1) or round(root2))

else:
    print("The equation has no real roots")

