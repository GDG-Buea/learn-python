# This a program  prompts the user to enter a four-digit integer and displays the number in reverse order

number = eval(input("Enter a four digit number: "))

position1 = number % 10

remainder1 = number // 10
position2 = remainder1 % 10

remainder2 = remainder1 // 10
position3 = remainder2 % 10

remainder3 = remainder2 // 10
position4 = remainder3

print("The reversed number is: ", str(position1) + str(position2) + str(position3) + str(position4))
