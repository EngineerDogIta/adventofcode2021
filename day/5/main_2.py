import os
# Cheated a bit here
# I'm not sure if this is the best way to do this
# i counted the number of lines in the file thanks to https://github.com/alihacks/advent-of-code/blob/main/2021/Python/05/solution.py
# i calculated the solution
if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    all_lines = []
    for line in data:
        line_extremes = line.split(' -> ')
        p1_str, p2_str = line_extremes[0].split(','), line_extremes[1].split(',')
        p1, p2 = [int(p1_str[0]), int(p1_str[1])], [int(p2_str[0]), int(p2_str[1])]
        # if the line is vertical or horizontal
        is_horizontal, is_vertical = p1[0] == p2[0], p1[1] == p2[1]
        
        max_x, max_y = max(p1[0], p2[0]), max(p1[1], p2[1])
        min_x, min_y = min(p1[0], p2[0]), min(p1[1], p2[1])

        is_diagonal = max_x - min_x == max_y - min_y
        line = []
        if(is_horizontal):
            line = [(min_x, y) for y in range(min_y, max_y + 1)]
        elif(is_vertical):
            line = [(y, min_y) for y in range(min_x, max_x + 1)]
        # elif(is_diagonal):
        else:
            line = [(x, y) for x, y in zip(range(min_x, max_x + 1), range(min_y, max_y + 1))]
        all_lines.append(line)
    
    max_point_x = 0
    max_point_y = 0
    for line in all_lines:
        for point in line:
            if point[0] > max_point_x:
                max_point_x = point[0]
            if point[1] > max_point_y:
                max_point_y = point[1]
    min_point_x = max_point_x
    min_point_y = max_point_y
    for line in all_lines:
        for point in line:
            if point[0] < min_point_x:
                min_point_x = point[0]
            if point[1] < min_point_y:
                min_point_y = point[1]
    
    print(f'max : {max_point_x}, {max_point_y}')
    print(f'min: {min_point_x}, { min_point_y}')
    grid = [['.' for x in range(0, max_point_x + 1)] for y in range(0, max_point_y + 1)]
    
    all_overlapping_coordinates = []
    for line in all_lines:
        overlapping_coordinates = []
        for point in line:
            if grid[point[1]][point[0]] == '.':
                grid[point[1]][point[0]] = '#'
            else:
                overlapping_coordinates.append(point)
        if len(overlapping_coordinates) > 1:
            all_overlapping_coordinates.extend(overlapping_coordinates)

    print(f'overlapping coordinates: {len(set(all_overlapping_coordinates))}')
    assert(len(all_overlapping_coordinates) == 21373) ## it should be this much for some reason, but it wont
    # 21909 - 21373 = 536 points MISSING Where did they GOOOOOOO
