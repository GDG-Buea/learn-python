# This program  prompts a user to enter a Social Security number in the format ddd-dd-dddd, where d is a digit.
#  The program displays the message Valid SSN for a correct Social Security number or Invalid SSN otherwise.


class SocialSecurityNumber:
    def __init__(self, ssn=''):
        self.__ssn_number = ssn

    def get_ssn(self):
        self.__ssn_number = input("Enter a social security number of the form ddd-dd-dddd:")

    def check_ssn_number(self):

        string1 = self.__ssn_number[0:3]
        string2 = self.__ssn_number[3]
        string3 = self.__ssn_number[4:6]
        string4 = self.__ssn_number[6]
        string5 = self.__ssn_number[7:11]

        if self.__ssn_number.__len__() == 11 and string1.isdigit() and '-' in string2 and string3.isdigit() \
                and '-' in string4 and string5.isdigit():
            print("Valid SSN")
        else:
            print("Invalid SSN")


def main():

    client1= SocialSecurityNumber()
    client1.get_ssn()
    client1.check_ssn_number()


main()




