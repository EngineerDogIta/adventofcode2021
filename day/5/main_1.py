import os
from Line import Line, Point

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    overlapping_lines = 0
    all_lines = []
    for line in data:
        line_points = line.split(' -> ')
        p1 = line_points[0].split(',')
        p2 = line_points[1].split(',')
        p1 = Point(int(p1[0]), int(p1[1]))
        p2 = Point(int(p2[0]), int(p2[1]))
        l1 = Line(p1, p2)
        if l1.is_horizontal() or l1.is_vertical():
            all_lines.append(l1)

    for i in range(len(all_lines)):
        for j in [k for k in range(len(all_lines)) if k != i]:
            if all_lines[i].overlaps(all_lines[j]):
                overlapping_lines += 1
                break


    print(f'overlapping_lines: {overlapping_lines}')
    print(f'number of lines that they overleap at least one time {len([x for x in all_lines if x.overlaps_with != None])}')
    print(f'overlapping_points {sum([x.number_of_overlaps(x.overlaps_with) for x in all_lines if x.overlaps_with != None])}')
    