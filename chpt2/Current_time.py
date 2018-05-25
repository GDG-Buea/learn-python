# This program displays the current time in GMT. It prompts the user to enter the time zone in hours away
# from (offset to) GMT and displays the time in the specified time zone

import time

timeZone = eval(input("Enter the time zone offset to GMT: "))

totalTime = time.time()

totalSeconds = int(totalTime)
currentSecond = (totalSeconds + timeZone * 3600) % 60

totalMinutes = totalSeconds // 60
currentMinute = (totalMinutes + timeZone * 60) % 60

totalHours = (totalMinutes // 60)
currentHour = (totalHours + timeZone) % 24


print("The current time is ", currentHour, ":", currentMinute, ":", currentSecond, "GMT")