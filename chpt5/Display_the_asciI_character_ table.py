# This program displays the characters in the ASCII character table from ! to ~ .
# It displays ten characters per line and each character is separated by exactly one space.

printSize = 10
count = 0
print()
for k in range(33, 127):
    print("\t", chr(k), end='' + "\t")
    count += 1

    if count % 10 == 0:
        print()

