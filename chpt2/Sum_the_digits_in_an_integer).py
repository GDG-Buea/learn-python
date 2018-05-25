# This  program  reads an integer between 0 and 1000 and adds all the digits in the integer.

number = eval(input("Enter a number between 0 and 1000: "))

unitRank = number % 10
number1 = number // 10

tenseRank = number1 % 10
number2 = number1 // 10

hundredRank = number2

summationOfNumber = unitRank + tenseRank + hundredRank

print("The sum of the digits is:", summationOfNumber)

