"""
https://adventofcode.com/2021/day/1
"""

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        rows = [int(x) for x in f.read().splitlines()]

    count = 0
    for i in range(3, len(rows)):
        sumthree = rows[i] + rows[i-1] + rows[i-2]
        sumthree_prec = rows[i - 1] + rows[i-2] + rows[i-3]
        if sumthree > sumthree_prec:
            count += 1

    print(count) # prints many sums that are larger than the previous sum