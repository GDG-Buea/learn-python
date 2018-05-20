# This program  displays the population for each of the next five years in the US given that
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# 365 days = 31536000 seconds

numberOfYears = 5
currentPopulation = 312032486
numberOfSecondsIn1year = 31536000

birthsPerYear = numberOfSecondsIn1year // 7
deathsPerYear = numberOfSecondsIn1year // 13
immigrantsPeryear = numberOfSecondsIn1year // 45

print("The population in ", numberOfYears, "years", "will be", currentPopulation +
      (numberOfYears * (birthsPerYear + immigrantsPeryear - deathsPerYear)), "people", "who are US citizens")

