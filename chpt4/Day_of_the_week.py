# This program prompts the user to enter a year, month, and day of the month, and then it displays
# the name of the day of the week.

year = eval(input("Enter the year(e.g. 2015): "))
month = eval(input("Enter the month(1-12):"))
day = eval(input("Enter day of the month(1-31): "))

century = (year // 100)
century_year = (year % 100)
dayOfTheWeek = (day + (26 * (month + 1)) // 10 + century_year + (century_year // 4) + (century // 4) + 5 * century) % 7

# If January or February is entered you must add
# 12 to the month and minus 1 from the year. This
# puts you in month 13 or 14 of previous year.

if month == 1:
    month = month + 12
    year = year - 1
elif month == 2:
    month = month + 12
    year = year - 1


if dayOfTheWeek == 0:
    print('Day of the week is Saturday')

elif dayOfTheWeek == 1:
    print('Day of the week is Sunday')

elif dayOfTheWeek == 2:
    print('Day of the week is Monday')

elif dayOfTheWeek == 3:
    print('Day of the week is Tuesday')

elif dayOfTheWeek == 4:
    print('Day of the week is Wednesday')

elif dayOfTheWeek == 5:
    print('Day of the week is Thursday')

elif dayOfTheWeek == 6:
    print('Day of the week is Friday')


