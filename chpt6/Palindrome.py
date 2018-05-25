
# This program prompts a user to enter an integer and reports whether the integer is a palindrome or not

#  A number is a palindrome if its reversal is the same as itself.


def reverse(number):
    position1 = number % 10

    remainder1 = number // 10
    position2 = remainder1 % 10

    remainder2 = remainder1 // 10
    position3 = remainder2

    return int(str(position1) + str(position2) + str(position3))


def is_palindrome(number):
    value = number
    if value == reverse(number):
        return 'This is a palindrome'
    else:
        return 'This is not a palindrome'


def main():
    number_test = eval(input("Enter a four digit number to test if it's a palindrome: "))
    print(is_palindrome(number_test))


main()