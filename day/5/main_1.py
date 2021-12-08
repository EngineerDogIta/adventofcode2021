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
        p1 = int(p1[0]), int(p1[1])
        p2 = int(p2[0]), int(p2[1])
        # if the line is vertical or horizontal
        is_horizontal = p1[0] == p2[0]
        is_vertical = p1[1] == p2[1]
        if is_horizontal or is_vertical:
            # get a list of points of the line from p1 to p2
            max_x = max(p1[0], p2[0])
            max_y = max(p1[1], p2[1])
            min_x = min(p1[0], p2[0])
            min_y = min(p1[1], p2[1])
            line = []
            if(is_horizontal):
                for y in range(min_y, max_y + 1):
                    line.append(Point(min_x, y))
            elif(is_vertical):
                for x in range(min_x, max_x + 1):
                    line.append(Point(x, min_y))
            all_lines.append(line)
    
    points = set()
    overlapping_points = set()
    for line in all_lines:
        for point in line:
            if point not in points:
                points.add(point)
            else:
                overlapping_points.add(point)
    
    overlapping_lines = len(overlapping_points)

    print(f'overlapping_lines: {overlapping_lines}')
    