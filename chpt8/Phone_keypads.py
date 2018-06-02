
# This program returns a number, given an uppercase letter. It prompts the user to enter a phone number as a string.
# The input number may contain letters. The program translates a letter (uppercase or
#  lowercase) to a digit and leaves all other characters intact.


def get_number(uppercase_letter):


    for ch in uppercase_letter:

        if ch.isalpha():

            character_to_number = ord(ch)

            print(character_to_number, end='')

        else:
            print(ch, end='')


def main():
    uppercase_letter = input("Enter a string: ")

    get_number(uppercase_letter)


main()