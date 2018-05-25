# This program finds the smallest integer n such that n2 is greater than 12,000


n = 0

while n ** 2 < 12000:
    n += 1

print(n)