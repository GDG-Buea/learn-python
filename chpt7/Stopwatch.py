# This program

import time


class StopWatch:
    def __init__(self, end_time=0, start_time=time.time()):
        self.__var1 = start_time
        self.__var2 = end_time

    def get_start_time(self):
        return self.__var1

    def get_end_time(self):
        return self.__var2

    def start(self):
        return time.time()

    def stop(self):
        return time.time()

    def get_elapsed_time(self):
        return int(self.get_start_time()) - int(self.get_end_time())


def main():

    duration_of_addition = StopWatch()
    duration_of_addition.start()

    sum = 0
    count = 0
    print()
    for i in range(1, 101):
        sum += i
        count += 1
        print("\t", format(i, "3d"), end=" | ")
        if count % 20 == 0:
            print()
    print()

    duration_of_addition.get_end_time()
    print("\t______________________________________________________________________________________________", end='_')
    print("\t________________________________________________________________")
    print()

    print("The time taken to add number from 1 to 1000,000 is: ", duration_of_addition.get_elapsed_time(),
          "milliseconds")
    print()
    print("This calculation takes ", duration_of_addition.get_elapsed_time() // 216000, "hours")


main()