# This program displays the price change percentage for the Intel Corporation Company that has a stock symbol of INTC,
# with the previous closing price of 20.5 , and the new current price of 20.35


class Stock:
    def __init__(self, symbol, name, previous_closing_price, current_price):
        self.__name = name
        self.__symbol = symbol
        self.__previous_closing_price = previous_closing_price
        self.__currentPrice = current_price

    def get_stock_name(self):
        return self.__name

    def get_stock_symbol(self):
        return self.__symbol

    def get_previous_closing_price(self):
        return self.__previous_closing_price

    def get_current_price(self):
        return self.__currentPrice

    def set_previous_closing_price(self, previous_price):
        self.__previous_closing_price = previous_price

    def set_current_price(self, current_price):
        self.__previous_closing_price = current_price

    def get_change_percent(self):
        return (self.__previous_closing_price - self.__currentPrice) / 100


def main():
    company1 = Stock("INTC", "Intel Corporation", 20.5, 20.35,)

    print("\n", company1.get_stock_name(), "with stock symbol ", company1.get_stock_symbol(),
          "has a price percentage change of ", format(company1.get_change_percent(), ".4f"), "%", "from ", "$",
          company1.get_previous_closing_price(), "to ", "$", company1.get_current_price())


main()