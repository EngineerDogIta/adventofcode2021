"""
https://adventofcode.com/2021/day/2
"""
depth = 0
horizontal = 0

if __name__ == '__main__':
    with open('input.txt', 'r', encoding='UTF-8') as f:
        data = [x.split(' ') for x in f.read().splitlines()]
    
    for move in data:
        if(move[0] == 'forward'):
            horizontal += int(move[1])
        elif(move[0] == 'down'):
            depth += int(move[1])
        elif(move[0] == 'up'):
            depth -= int(move[1])
    
    print(f'depth {depth}, horizontal {horizontal}')
    print(f'depth * horizontal {depth*horizontal}')