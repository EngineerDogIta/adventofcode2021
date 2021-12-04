"""
https://adventofcode.com/2021/day/1
"""

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        rows = [int(x) for x in f.read().splitlines()]

    count = 0
    for i in range(1, len(rows)):
        if rows[i] > rows[i-1]:
            count += 1

    print(count) # prints many measurements larger than the previous measurement