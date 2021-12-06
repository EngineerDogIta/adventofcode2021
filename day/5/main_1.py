import os
from Line import Line, Point

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    lines = []
    for line in data:
        points = line.split(' -> ')
        p1 = points[0].split(',')
        p2 = points[1].split(',')
        p1 = Point(int(p1[0]), int(p1[1]))
        p2 = Point(int(p2[0]), int(p2[1]))
        line_points = Line(p1, p2)
        if line_points.is_vertical() or line_points.is_horizontal():
            lines.append(line_points)

    overlapping_lines = 0
    
    for i1 in range(len(lines)):
        for i2 in range(len(lines)):
            if i1 != i2:
                line1 = lines[i1]
                line2 = lines[i2]
                if line1.overlaps(line2):
                    overlapping_lines += 1

    print(f'Overlapping lines: {overlapping_lines}')
