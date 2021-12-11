import os
from Lanternfish import Lanternfish

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()

    fishes = [Lanternfish(int(x)) for x in data[0].split(',')]

    for day in range(256):
        lanternfish_2add = []
        for i_fish in range(len(fishes)):
            new_fish = fishes[i_fish].pass_a_day()
            if new_fish != None:
                lanternfish_2add.append(new_fish)
        fishes.extend(lanternfish_2add)
        print(f'Day {day} passed {len(fishes)} fishes')

    print(f'Number of fishes after 80 days {len(fishes)}')