import os
from collections import Counter

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    fishes = [int(x) for x in data[0].split(',')]
    # fishes = [3,4,3,1,2]
    fishes_counter = {x: 0 for x in range(9)}
    fishes_counter.update(dict(Counter(fishes)))

    # print(','.join([str(x) for x in range(9)]))
    # print(','.join([str(fishes_counter[x]) for x in range(9)]))

    # days = 84

    days = 256

    for i in range(days):
        # print(f'Day {i} len {fishes_counter}')
        zero_counter = fishes_counter[0]

        new_fishes_counter = {x: 0 for x in range(9)}

        for counter in range(1,9):
            new_fishes_counter[counter-1] = fishes_counter[counter]
        new_fishes_counter[8] = zero_counter
        new_fishes_counter[6] += zero_counter

        fishes_counter = new_fishes_counter
        # print(','.join([str(fishes_counter[x]) for x in range(9)]))
    
    print(f'Number of fishes after {days} days: {sum(fishes_counter.values())}')
