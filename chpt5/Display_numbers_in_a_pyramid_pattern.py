# This program uses for loops to display the pyramid pattern below that has eight lines and is bounded by 1

fixedPyramidSize = 8


for i in range(1, fixedPyramidSize + 1):

    # spaces to the left
    for j in range((fixedPyramidSize + 1) - i, 1, -1):
        print(" ", end=" ")

    # printing numbers to the left

    for k in range(0, i - 1):
        print(format(2 ** k, "1d"), end=" ")
    # printing numbers to the right

    for l in range(i - 1, -1, -1):
        print(format(2 ** l, "1d"), end=" ")

    print()



