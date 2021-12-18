import os
from collections import Counter

def get_near_basins(coordinate, dict_heightmap, heatmap_points:dict):
    this_point = {coordinate : dict_heightmap[coordinate]}

    points_of_directions = {}
    up_dir    = (coordinate[0]  , coordinate[1]-1)
    down_dir  = (coordinate[0]  , coordinate[1]+1)
    left_dir  = (coordinate[0]-1, coordinate[1])
    right_dir = (coordinate[0]+1, coordinate[1])

    if up_dir in dict_heightmap.keys():
        heightpoint_val = dict_heightmap[up_dir]
        if heightpoint_val != 9 and up_dir not in heatmap_points.keys():
            points_of_directions[up_dir] = dict_heightmap[up_dir]

    if down_dir in dict_heightmap.keys():
        heightpoint_val = dict_heightmap[down_dir]
        if heightpoint_val != 9 and down_dir not in heatmap_points.keys():
            points_of_directions[down_dir] = dict_heightmap[down_dir]

    if left_dir in dict_heightmap.keys():
        heightpoint_val = dict_heightmap[left_dir]
        if heightpoint_val != 9 and left_dir not in heatmap_points.keys():
            points_of_directions[left_dir] = dict_heightmap[left_dir]

    if right_dir in dict_heightmap.keys():
        heightpoint_val = dict_heightmap[right_dir]
        if heightpoint_val != 9 and right_dir not in heatmap_points.keys():
            points_of_directions[right_dir] = dict_heightmap[right_dir]

    assert(len(points_of_directions.keys()) < 5)
    
    # check_nearest_list = [dict_heightmap[coordinate] <= point_value for point_value in points_of_directions.values()]
    # check_low_basins = all(check_nearest_list)
    
    if dict_heightmap[coordinate] != 9: # and check_low_basins:
        heatmap_points.update(this_point)
    
    if len(points_of_directions) > 0:
        for direction in points_of_directions.keys():
            heatmap_points.update(get_near_basins(direction, dict_heightmap, heatmap_points))
    
    return heatmap_points 

class Basin:
    def __init__(self, coordinates: dict):
        self.coordinates = coordinates
    
    def __str__(self):
        return str(self.coordinates)

    def __repr__(self):
        return f'Basin({self.coordinates})'

    def __eq__(self, other):
        return set(self.coordinates.keys()) == set(other.coordinates.keys())
    
    def __hash__(self) -> int:
        """
        This is needed for the set() to work.
        >>> Basin({(0,0):0, (0,1):1, (1,0):2, (1,1):3})
        Basin({(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3})
        >>> Basin({(0,0):0, (0,1):1, (1,0):2, (1,1):3}) == Basin({(0,0):0, (0,1):1, (1,0):2, (1,1):3})
        True
        >>> Basin({(0,0):0, (0,1):1, (1,0):2, (1,1):3}) == Basin({(0,0):0, (0,1):1, (1,0):2, (1,1):4})
        True
        >>> Basin({(0,0):0, (0,1):1, (1,0):2, (1,1):3}) == Basin({(0,0):0, (0,1):1, (1,0):2, (1,1):3, (2,0):4})
        False
        """
        return hash(tuple(map(hash, self.coordinates.keys())))
    
    def __len__(self) -> int:
        return len(self.coordinates.keys())

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    heightmap = ['2199943210',
                 '3987894921',
                 '9856789892',
                 '8767896789',
                 '9899965678']
    # heightmap = data

    dict_heightmap = {}

    max_y = len(heightmap)
    max_x = len(heightmap[0])
    for y in range(max_y):
        for x in range(max_x):
            dict_heightmap[(x, y)] = int(heightmap[y][x])

    # Top-left basins
    basins = set()
    for y in range(max_y):
        for x in range(max_x):
            basins.add(Basin(get_near_basins((x, y), dict_heightmap, {})))
    # top_left = get_near_basins((0, 0), dict_heightmap, {})
    # bottom_left = get_near_basins((0, max_y-1), dict_heightmap, {})
    # bottom_right = get_near_basins((max_x-1, max_y-1), dict_heightmap, {})
    # top_right = get_near_basins((max_x-1, 0), dict_heightmap, {})

    lenghts_basins = {len(basin) for basin in basins}
    first_three_highest = sorted(list(lenghts_basins), reverse=True)[:3]
    print(f'Result of part 2 is: {(first_three_highest[0] * first_three_highest[1] * first_three_highest[2])}')

    # for y in range(max_y):
    #     for x in range(max_x):
    #         if (x, y) in basins:
    #             print('#', end='')
    #         else:
    #             print(f'{dict_heightmap[(x, y)]}', end='')
    #     print()
    assert((first_three_highest[0] * first_three_highest[1] * first_three_highest[2]) == 1134)
