
# This is a modified version of exercise 1.11. that prompts the user to enter the
# number of years and displays the population after that many years in the US given that
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# 365days = 31536000 seconds
# Number of births in 1year = 494
# Number of immigrants in 1year = 77
# Number of deaths in 1year = 266


numberOfYears = eval(input("Enter the number of years: "))

currentPopulation = 312032486
numberOfSecondsIn1year = 31536000

birthsPerYear = numberOfSecondsIn1year // 7
deathsPerYear = numberOfSecondsIn1year // 13
immigrantsPeryear = numberOfSecondsIn1year // 45

print("The population in ", numberOfYears, "years","will be", currentPopulation +
      (numberOfYears * (birthsPerYear + immigrantsPeryear - deathsPerYear)), "people")



