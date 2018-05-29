# This program depicts a bank account with an account id of 1122, a  balance of $20,000, and an
# annual interest rate of 4.5%.
# A withdrawal of $2,500 is made and a  deposit $3,000, and print the id, balance, monthly interest rate,
# and monthly interest of this account is printed to the screen


class Account:
    def __init__(self, account_id=0, balance=100.0, annual_interest_rate=0.0, withdrawal=0, deposit=0):
        self.__account_id = account_id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def get_account_id(self):
        return self.__account_id

    def get_balance(self):
        return self.__balance

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def set_account_id(self, account_id):
        self.__account_id = account_id

    def set_balance(self, balance):
        self.__balance = balance

    def set_annual_interest_rate(self, annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate

    def get_monthly_interest_rate(self):
        return (self.get_annual_interest_rate() / 100) / 12

    def get_monthly_interest(self):
        return self.__balance * self.get_monthly_interest_rate()

    def withdraw(self, withdraw_amount):
        self.__balance -= withdraw_amount

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount


def main():
    account1 = Account(122, 20000, 45)
    account1.withdraw(2500)
    account1.deposit(3000)

    print()

    print("\nAccount number:", account1.get_account_id(), "\t|\thas a balance=", "$", account1.get_balance(),
          "\t|\tmonthly interest rate=", account1.get_monthly_interest_rate(), "\t|\tand monthly interest=", "$",
          account1.get_monthly_interest())

    print()


main()


