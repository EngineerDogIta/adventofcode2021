import os

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()
        
    crabs_x = [int(x) for x in data[0].split(',')]
    # crabs_x = [16,1,2,0,4,2,7,1,2,14]

    fuel = 0
    min_pos = min(crabs_x)
    max_pos = max(crabs_x) + 1
    possible_fuel_burn = []
    for pos in range(min_pos, max_pos):
        distance_from_pos = [abs(pos - int(x)) for x in crabs_x]
        possible_fuel_burn.append(sum([sum(list(range(distance+1))) for distance in distance_from_pos]))
    fuel = min(possible_fuel_burn)

    print(f'Fuel used {fuel}')