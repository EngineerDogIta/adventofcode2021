
depth = 0
horizontal = 0
aim = 0

if __name__ == '__main__':
    with open('input.txt', 'r', encoding='UTF-8') as f:
        data = [x.split(' ') for x in f.read().splitlines()]

    for move in data:
        if(move[0] == 'forward'):
            horizontal += int(move[1])
            depth += aim * int(move[1])
        elif(move[0] == 'down'):
            aim += int(move[1])
        elif(move[0] == 'up'):
            aim -= int(move[1])
    
    print(f'{horizontal} {depth} {aim}')
    
    print(f'depth * horizontal {depth*horizontal}')