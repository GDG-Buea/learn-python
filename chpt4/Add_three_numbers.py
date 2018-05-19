# This  program  generates three integers and prompts the user to enter the sum of these  integers.

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

userReply = eval(input("What is the sum of " + str(number1) + "+" + str(number2) + "+" + str(number3) + "  "))

print("The sum of ", number1, "+", number2, "+", number3, "=", number1 + number2 + number3, "is",
      number1 + number2 + number3 == userReply)
