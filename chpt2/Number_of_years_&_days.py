# This program prompts a user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes

minutes = eval(input("Enter the number of minutes: "))
inputMinutes = int (minutes)

hours = inputMinutes // 60
days = hours // 24
years = days // 365

daysLeft = round(days % 365)

print(days)
print(inputMinutes, "minutes", " is approximately ", years, "years", daysLeft, "days")