# This program  generates two integers under 100 and prompts the user to enter the sum of these two integers.
#  The program then reports true if the answer is correct, false otherwise.

import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)


userReply = eval(input("What is the sum of " + str(number1) + " + " + str(number2) + "  "))

print("Your answer is ", number1 + number2 == userReply)
