#!/usr/bin/python3
import os
from BingoBoard import BingoBoard

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()

    bingo_numbers = [int(x) for x in data[0].split(',')]

    bingo_boards = [BingoBoard([[int(num) for num in data[i].split(' ') if num != ''] for i in range(i_data+1, i_data+6)]) for i_data in range(1, len(data), 6)]

    winner = None
    last_extracted_number = None

    for extracted_num in bingo_numbers:
        last_extracted_number = extracted_num
        for i in range(len(bingo_boards)):
            bingo_boards[i].mark_number(extracted_num)
        for i in range(len(bingo_boards)):
            if (bingo_boards[i].is_winner()):
                print(f'Player {i+1} won!')
                winner = bingo_boards[i]
                break
        if winner:
            break

    print(f'Sum of unmarked numbers: {winner.sum_unmarked()}')
    print(f'Last extracted number: {last_extracted_number}')
    print(f'his final score is: {winner.score(last_extracted_number)}')