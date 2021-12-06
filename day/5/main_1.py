import os
# from Line import Line, Point

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    # lines = []
    # for line in data:
    #     points = line.split(' -> ')
    #     p1 = points[0].split(',')
    #     p2 = points[1].split(',')
    #     p1 = Point(int(p1[0]), int(p1[1]))
    #     p2 = Point(int(p2[0]), int(p2[1]))
    #     line_points = Line(p1, p2)
    #     if line_points.is_vertical() or line_points.is_horizontal():
    #         lines.append(line_points)
    grid = {(0, 0): 0}
    all_lines = []
    for line in data:
        points = line.split(' -> ')
        p1 = points[0].split(',')
        p2 = points[1].split(',')
        p1 = (int(p1[0]), int(p1[1]))
        p2 = (int(p2[0]), int(p2[1]))
        line_points = (p1, p2)
        if p1[0] == p2[0]:
            all_lines.append(line_points)
            from_y, to_y = min(p1[1], p2[1]), max(p1[1], p2[1])
            if from_x != to_x:
                for ys in range(from_x, to_x):
                    if (ys, p1[0]) in grid.keys():
                        grid[(ys, p1[0])] += 1
                    else:
                        grid[(ys, p1[0])] = 1
            else:
                grid[p1] += 1
        elif p1[1] == p2[1]:
            all_lines.append(line_points)
            from_x, to_x = min(p1[0], p2[0]), max(p1[0], p2[0])
            if from_x != to_x:
                for xs in range(from_x, to_x):
                    if (p1[1], xs) in grid.keys():
                        grid[(p1[1], xs)] += 1
                    else:
                        grid[(p1[1], xs)] = 1
            else:
                grid[p1] += 1

    overlapping_lines = 0
    for point in grid.keys():
        if grid[point] == 2:
            overlapping_lines += 1
    print(f'overlapping_lines: {overlapping_lines}')

    # represent the grid
    min_x = min(grid.keys(), key=lambda x: x[0])[0]
    max_x = max(grid.keys(), key=lambda x: x[0])[0]
    min_y = min(grid.keys(), key=lambda x: x[1])[1]
    max_y = max(grid.keys(), key=lambda x: x[1])[1]

    for x in range(min_x, max_x + 1):
        for ys in range(min_y, max_y + 1):
            if (ys, x) in grid.keys():
                print(grid[(ys, x)], end='')
            else:
                print('.', end='')
        print()

    # overlapping_lines = 0
    
    # for i1 in range(len(lines)):
    #     for i2 in range(len(lines)):
    #         if i1 != i2:
    #             line1 = lines[i1]
    #             line2 = lines[i2]
    #             if line1.overlaps(line2):
    #                 overlapping_lines += 1

    # print(f'Overlapping lines: {overlapping_lines}')
