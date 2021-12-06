#!/usr/bin/python3
import os
from BingoBoard import BingoBoard
"""
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

"""
if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()

    bingo_numbers = [int(x) for x in data[0].split(',')]

    bingo_boards = [BingoBoard([[int(num) for num in data[i].split(' ') if num != ''] for i in range(i_data+1, i_data+6)]) for i_data in range(1, len(data), 6)]

    last_winner = None
    last_extracted_number = None

    """
    for each bingo_number, mark the bingo_boards,
    get the score from the last winning board
    """
    for bingo_number in bingo_numbers:
        for bingo_board in bingo_boards:
            if not bingo_board.has_won:
                bingo_board.mark_number(bingo_number)
                if bingo_board.is_winner():
                    last_winner = bingo_board
                    last_extracted_number = bingo_number
    print(f'Player with the board \n{last_winner}\n is the last winner!')

    print(f'Sum of unmarked numbers: {last_winner.sum_unmarked()}')
    print(f'Last extracted number: {last_extracted_number}')
    print(f'his final score is: {last_winner.score(last_extracted_number)}')


# Player
# 3        X       X       X       X
# X       78      X       X       X
# X       X       23      X       X
# X       79      X       X       X
# X       X       X       80      X is the last winner!
# Sum of unmarked numbers: 263
# Last extracted number: 86
# his final score is: 22618