# This program prompts the user to enter a three-digit number and determines whether the user wins according
#  to the following rules:
# 1. If the user input matches the lottery number in the exact order, the award is
# $10,000.
# 2. If all the digits in the user input match all the digits in the lottery number, the
# award is $3,000.
# 3. If one digit in the user input matches a digit in the lottery number, the award is
# $1,000.

import random

lotteryNumber = random.randrange(000, 999)
userReply = eval(input("What is the wining number? "))

lotteryNumberRemainder1 = lotteryNumber // 100           #first digit
lotteryNumberRemainderA = lotteryNumber % 100
lotteryNumberRemainder2 = lotteryNumberRemainderA // 10  #second digit
lotteryNumberRemainder3 = lotteryNumberRemainderA % 10   #third digit

userReplydigit1 = userReply // 100   #first digit
userReplydigitA = userReply % 100
userReplydigit2 = userReplydigitA // 10   #second digit
userReplydigit3 = userReplydigitA % 10  #third digit


if userReply == lotteryNumber:
    print("Exact match, you have won $10,000")

elif lotteryNumberRemainder1 == userReplydigit1 or lotteryNumberRemainder2 == userReplydigit2 or \
     lotteryNumberRemainder3 == userReplydigit3:
    print("Cool match, you won $1,000.")

elif lotteryNumberRemainder1 == userReplydigit1 and lotteryNumberRemainder2 == userReplydigit2 and \
     lotteryNumberRemainder3 == userReplydigit3:
    print("Cool match , you won $3,000.")

else:
    print("You lost")
    print("The wining answer is: ", lotteryNumber)
