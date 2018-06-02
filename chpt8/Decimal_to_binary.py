
# This program parses a decimal number into a binary number as a string.
# The user is prompted to enter a decimal integer value and displays the corresponding binary value.


def decimal_to_binary():

    value = int(input('please enter the no. in decimal format: '))

    x = value
    k = []

    while value > 0:
        remainder = int(float(value % 2))
        k.append(remainder)
        value = (value - remainder) / 2

    k.append(0)
    string = ""

    for j in k[::-1]:
        string = string + str(j)
    print('The binary no. for %d is %s' % (x, string))


decimal_to_binary()