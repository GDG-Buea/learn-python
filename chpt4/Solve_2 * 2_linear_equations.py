# This program that prompts the user to enter a , b , c , d , e , and f and display the result.
#  If ad – bc is 0 , report that The equation has no solution


a, b, c, d, e, f = eval(input("Enter the values for a, b, c, d, e and f: "))

x = (e * d - b * f) / (a * d - b * c)

y = (a * f - e * c) / (a * d - b * c)

if a * d - b * c == 0:
    print("The equation has no solution")

else:
    print("x" + " is " + format(x, ".1f") + " and " + "y"+ " is " + format(y, ".1f"))
