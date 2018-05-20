# This program prompts the user to enter an integer from 1 to 15 and displays a pyramid,

pyramidSize = int(eval(input("Enter the number of lines you want your pyramid to have: ")))

for i in range(1, pyramidSize + 1):

    # spaces to the left and right
    for j in range(1, (pyramidSize + 1) - i):
        print(" ", end=" ")

    # printing numbers to the left

    for k in range(i, 1, -1):
        print(format(k, "1d"), end=" ")
    # printing numbers to the right

    for l in range(1, i + 1):
        print(format(l, "1d"), end=" ")

    print()
