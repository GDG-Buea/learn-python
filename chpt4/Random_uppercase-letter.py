# This program t displays a random uppercase letter.

import random

number = random.randint(97, 123)
letter = chr(number)

print(letter.upper())

