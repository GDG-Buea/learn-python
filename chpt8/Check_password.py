# This program prompts the user to enter a password and displays valid  password if the rules are followed
#  or invalid password otherwise.
# The password rules are as follows:
# A password must have at least eight characters.
# A password must consist of only letters and digits.
# A password must contain at least two digits


class Password:
    def __init__(self, password=''):
        self.__pass = password

    def get_password(self):
        self.__pass = input("Enter your password: ")

    def check_password(self):

        if self.__pass.__len__() == 8 and self.__pass.isalnum() and len([b for b in self.__pass if b.isdigit()]) == 2:
            print("Valid password")
            print()
        else:
            print("Invalid password\nPassword should contain atleast eight characters\nIt should contain letters and "
                  " at least two digits")


def main():

    client1 = Password()
    client1.get_password()
    client1.check_password()


main()

