import os
from Line import Point
from collections import Counter

points = set()
counter_overlaps = Counter()

def distribute_point(x, y):
    point = Point(x, y)
    counter_overlaps.update([point])

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    overlapping_lines = 0
    all_lines = []
    for line in data:
        line_extremes = line.split(' -> ')
        p1_str, p2_str = line_extremes[0].split(','), line_extremes[1].split(',')
        p1, p2 = [int(p1_str[0]), int(p1_str[1])], [int(p2_str[0]), int(p2_str[1])]
        # if the line is vertical or horizontal
        is_horizontal, is_vertical = p1[0] == p2[0], p1[1] == p2[1]

        max_x, max_y = max(p1[0], p2[0]), max(p1[1], p2[1])
        min_x, min_y = min(p1[0], p2[0]), min(p1[1], p2[1])

        if(is_horizontal):
            for y in range(min_y, max_y + 1):
                distribute_point(min_x, y)
                assert(min_y <= y <= max_y)
        elif(is_vertical):
            for x in range(min_x, max_x + 1):
                distribute_point(x, min_y)
                assert(min_x <= x <= max_x)
        else: #(is_diagonal):
            for x, y in zip(range(min_x, max_x + 1), range(min_y, max_y + 1)):
                distribute_point(x, y)
                assert(min_x <= x <= max_x)
                assert(min_y <= y <= max_y)
        

    print(f'overlapping_lines: {len([count for _, count in counter_overlaps.items() if count > 1])}')
    