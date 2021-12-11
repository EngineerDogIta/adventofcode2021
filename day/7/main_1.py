import os

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()
    crabs_x = [int(x) for x in data[0].split(',')]
    fuel = 0
    min_pos = min(crabs_x)
    max_pos = max(crabs_x) +1
    fuel = min([sum([abs(pos - int(x)) for x in crabs_x]) for pos in range(min_pos, max_pos)])

    print(f'Fuel used {fuel}')