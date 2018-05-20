# This program prompts the user to enter an integer for today’s day of the week
# (Sunday is 0, Monday is 1, ..., and Saturday is 6).
# Also it prompts the user to enter the number of days after today for a future day and displays
#  the future day of the week
import sys

todaysDay = eval(input("Enter a number for a day of the week (between 0 and 6): "))

if todaysDay == 0:
    print("The day of the week is Sunday")

elif todaysDay == 1:
    print("The day of the week is Monday")

elif todaysDay == 2:
    print("The day of the week is Tuesday")

elif todaysDay == 3:
    print("The day of the week is Wednesday")

elif todaysDay == 4:
    print("The day of the week is Thursday")

elif todaysDay == 5:
    print("The day of the week is Friday")

elif todaysDay == 6:
    print("The day of the week is Saturday")

else:
    print("The number you entered does not represent a valid day of the week")

numberDays = eval(input("Enter the number of days after today for a future day: "))
futureDay = numberDays + todaysDay

if futureDay == 0 or futureDay == 7:
    numberDays = 'Zero'
    print(numberDays, " days from  today will be Sunday")

elif futureDay == 1 or futureDay == 8:
    numberDays = 'One'
    print(numberDays, "day from  today will be Monday")

elif futureDay == 2 or futureDay == 9:
    numberDays = 'Two'
    print(numberDays, "days from  today will be Tuesday")

elif futureDay == 3 or futureDay == 10:
    numberDays = 'Three'
    print(numberDays, "days from  today will be Wednesday")

elif futureDay == 4 or futureDay == 11:
    numberDays = 'Four'
    print(numberDays, "days from  today will be Thursday")

elif futureDay == 5 or futureDay == 12:
    numberDays = 'Five'
    print(numberDays, "days from  today will be Friday")

elif futureDay == 6 or futureDay == 13:
    numberDays = 'Six'
    print(numberDays, "days from  today will be Saturday")

else:
    print("The number you entered does not represent a valid day of the week")
