# This program reads an unspecified number of integers,determines how many positive and negative values have been read,
#  and computes the total and average of the input values (not counting zeros).
# The program ends with the input 0 and the average is displayed as a floating-point number

userInput = 1
positiveCount = 0
negativeCount = 0
total = 0
average = 0

while userInput != 0:
    userInput = eval(input("Enter an integer, the input ends if it is 0: "))
    if userInput > 0:
        positiveCount += 1
    elif userInput < 0:
        negativeCount += 1
    else:
        continue
    total += userInput
    if userInput == 0:
        continue

print("The number of positives is: ", positiveCount)
print("The number of negatives is: ", negativeCount)
average = total / (positiveCount + negativeCount)
print("The total is: ", total)
print("The average is: ", average)


