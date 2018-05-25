#
# This program is a function that displays the first 100 pentagonal numbers with 10 numbers on each line.

#  A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on.
# So, the first few numbers are 1, 5, 12, 22, ....


def get_pentagonal_number(n):
    pentagonal_number = round(n * (3 * n - 1) / 2)
    print(format(pentagonal_number, '5d'), end='  ')


def main():
    count = 0
    for i in range(1, 101):
        if count % 10 == 0:
            print()
        get_pentagonal_number(i)
        count += 1


main()
