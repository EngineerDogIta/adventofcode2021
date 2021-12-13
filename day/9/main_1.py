import os
from collections import Counter

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    # heightmap = ['2199943210',
    #              '3987894921',
    #              '9856789892',
    #              '8767896789',
    #              '9899965678']
    heightmap = data

    dict_heightmap = {}

    sum_all_low_points = 0
    max_y = len(heightmap)
    max_x = len(heightmap[0])
    for y in range(max_y):
        for x in range(max_x):
            dict_heightmap[(x, y)] = int(heightmap[y][x])

    for y in range(max_y):
        for x in range(max_x):
            low_point = dict_heightmap[(x, y)]
            down = None
            if (x, y-1) in dict_heightmap.keys():
                down = dict_heightmap[(x, y-1)]
            up = None
            if (x, y+1) in dict_heightmap.keys():
                up = dict_heightmap[(x, y+1)]
            left = None
            if (x-1, y) in dict_heightmap.keys():
                left = dict_heightmap[(x-1, y)]
            right = None
            if (x+1, y) in dict_heightmap.keys():
                right = dict_heightmap[(x+1, y)]

            smoke_flows = [j for j in [up, down, left, right] if j != None]
            if all([low_point < j for j in smoke_flows]):
                sum_all_low_points += (low_point+1)
                print(f'{low_point}', end='')
            else:
                print('_', end='')

        print('')

    print(f'sum_all_low_points : {sum_all_low_points}')

    # assert(sum_all_low_points == 15)
