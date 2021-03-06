class BingoBoard:
    """
    Bingo Board Class,
    stores the numbers of the bingo board
    >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
    >>> bingo_board.board
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    >>> bingo_board.rows
    5
    >>> bingo_board.columns
    5
    >>> bingo_board.marked_numbers
    []
    """
    def __init__(self, board: list):
        self.board = board
        self.rows = len(self.board)
        self.columns = len(self.board[0])
        self.marked_numbers = []
        self.has_won = False

    def __str__(self):
        """
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> str(bingo_board)
        '1\\t2\\t3\\t4\\t5\\n6\\t7\\t8\\t9\\t10\\n11\\t12\\t13\\t14\\t15\\n16\\t17\\t18\\t19\\t20\\n21\\t22\\t23\\t24\\t25'
        """
        return str("\n".join(["\t".join(['X' if number in self.marked_numbers else str(number) for number in row]) for row in self.board]))

    def mark_number(self, number: int):
        """
        Mark a number on the board
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.mark_number(1)
        >>> str(bingo_board)
        'X\\t2\\t3\\t4\\t5\\n6\\t7\\t8\\t9\\t10\\n11\\t12\\t13\\t14\\t15\\n16\\t17\\t18\\t19\\t20\\n21\\t22\\t23\\t24\\t25'
        >>> bingo_board.mark_number(10)
        >>> str(bingo_board)
        'X\\t2\\t3\\t4\\t5\\n6\\t7\\t8\\t9\\tX\\n11\\t12\\t13\\t14\\t15\\n16\\t17\\t18\\t19\\t20\\n21\\t22\\t23\\t24\\t25'
        """
        self.marked_numbers.append(number)

    def is_marked(self, number: int):
        """
        Check if a number is marked on the board
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.is_marked(1)
        False
        >>> bingo_board.mark_number(1)
        >>> bingo_board.is_marked(1)
        True
        """
        return number in self.marked_numbers

    def is_row_marked(self, row: int):
        """
        Check if a row is marked on the board
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.is_row_marked(0)
        False
        >>> bingo_board.mark_number(1)
        >>> bingo_board.is_row_marked(0)
        False
        >>> bingo_board.mark_number(1)
        >>> bingo_board.mark_number(2)
        >>> bingo_board.mark_number(3)
        >>> bingo_board.mark_number(4)
        >>> bingo_board.mark_number(5)
        >>> bingo_board.is_row_marked(0)
        True
        >>> bingo_board.mark_number(11)
        >>> bingo_board.mark_number(12)
        >>> bingo_board.mark_number(13)
        >>> bingo_board.mark_number(14)
        >>> bingo_board.is_row_marked(2)
        False
        >>> bingo_board.mark_number(15)
        >>> bingo_board.is_row_marked(2)
        True
        """
        return all([self.is_marked(number) for number in self.board[row]])
    
    def rotate_board(self):
        """
        Rotate rows into columns
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> BingoBoard(bingo_board.rotate_board()).board
        [[1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25]]
        """
        rotated = [[row_board[icol] for row_board in self.board] for icol in range(self.columns)]
        return rotated

    def is_column_marked(self, column: int):
        """
        Check if a column is marked on the board
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.is_column_marked(0)
        False
        >>> bingo_board.mark_number(1)
        >>> bingo_board.mark_number(6)
        >>> bingo_board.mark_number(11)
        >>> bingo_board.is_column_marked(0)
        False
        >>> bingo_board.mark_number(16)
        >>> bingo_board.mark_number(21)
        >>> bingo_board.is_column_marked(0)
        True
        """
        return all([self.is_marked(number) for number in self.rotate_board()[column]])

    def is_winner(self):
        """	
        Check if the board is a winner
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.is_winner()
        False
        >>> bingo_board.mark_number(1)
        >>> bingo_board.mark_number(2)
        >>> bingo_board.mark_number(3)
        >>> bingo_board.mark_number(4)
        >>> bingo_board.mark_number(5)
        >>> bingo_board.is_winner()
        True
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.is_winner()
        False
        >>> bingo_board.mark_number(1)
        >>> bingo_board.mark_number(6)
        >>> bingo_board.mark_number(11)
        >>> bingo_board.mark_number(16)
        >>> bingo_board.mark_number(21)
        >>> bingo_board.is_winner()
        True
        """
        for nrow in range(self.rows):
            if self.is_row_marked(nrow):
                self.has_won = True
                return True
        for ncol in range(self.columns):
            if self.is_column_marked(ncol):
                self.has_won = True
                return True
        return False

    def sum_unmarked(self):
        """Sums all unmarked numbers on the board
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.sum_unmarked()
        325
        >>> bingo_board.mark_number(1)
        >>> bingo_board.mark_number(2)
        >>> bingo_board.mark_number(3)
        >>> bingo_board.mark_number(4)
        >>> bingo_board.mark_number(5)
        >>> bingo_board.sum_unmarked()
        310
        """
        listnumbers = [int(i) for i in (",".join([",".join([str(number) for number in row]) for row in self.board])).split(",")]
        return sum([number for number in listnumbers if not self.is_marked(number)])

    def score(self, extracted_number: int):
        """
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board.score(1)
        325
        >>> bingo_board.mark_number(1)
        >>> bingo_board.mark_number(2)
        >>> bingo_board.mark_number(3)
        >>> bingo_board.mark_number(4)
        >>> bingo_board.mark_number(5)
        >>> bingo_board.score(2)
        620
        >>> bingo_board.mark_number(16)
        >>> bingo_board.mark_number(21)
        >>> bingo_board.score(1)
        273
        """
        return self.sum_unmarked() * extracted_number

    def __eq__(self, __o: object):
        """Two boards are equal if they have the same rows
        >>> bingo_board = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board2 = BingoBoard([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
        >>> bingo_board == bingo_board2
        True
        """
        return self.board == __o.board

if __name__ == "__main__":
    import doctest
    doctest.testmod()