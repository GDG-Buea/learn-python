# This program  receives an ASCII code (an integer between 0 and 127 ) and displays its character. For example, if the
# user enters 97 , the program displays the character a .

code = eval(input("Enter an ASCII code: "))

result = chr(code)

print("The character is: ", result)
