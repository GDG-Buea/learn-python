# This program displays  two tables side by side, which depict the conversion of kilograms to pounds and vice versa
#  1 mile is 1.609 kilometers and that 1 kilometer is .621 mile):

i = 1
j = 20
print()

print(format("Kilograms", "9s"), "\t\t", format("Pounds", "6s"), "\t\t|", format("\t\tPounds", "6s"), "\t\t\t\t",
      format("Kilograms", "9s"))
print()

for i in range(1, 200):
    print(format(i, "1d"), "\t\t\t\t", format(i * 2.2, "1.1f"), "\t\t\t|\t\t", format(j, "1d"), "\t\t\t\t",
          format(j * 0.45, "1.2f"))
    i += 2
    j += 5


