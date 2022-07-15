"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other
words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k
rows, 1 column), where k can be of any size. At least one horizontal or
vertical cell separates between two battleships (i.e., there are no adjacent
battleships).

"""

"""
Very simple principle:
Identify just the left-most, or top-most cell of any given battleship,
and count that when it is encountered.

The left-most is the X occuring at i = 0 or for which board[i-1][j] == '.'
The top-most is the X occuring at j = 0 or for which board[i][j-1] == '.'


"""


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == 'X'
                        and (i == 0 or board[i-1][j] == '.')
                        and (j == 0 or board[i][j-1] == '.')):
                    count += 1
        
        return count


"""
Count the battleships
Use a prev variable to indicate whether the previous was an X

Traverse in row-major order

When an X is encountered, it is either a horizontal or vertical battleship.
You could assume it is horizontal, but check vertical if length = 1
And, if horizontal length = 1:
    if cell below is '.': increment count
    else: do nothing # will catch it in the next row


For each row, we maintain a variable horz_ship_len, representing the horizontal length
of the current ship which overlaps the cell we are in
or, zero if we are not in a ship

1.

"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        nrows = len(board)
        if nrows == 0:
            return 0
        ncols = len(board[0])
        horz_ship_len = 0
        num_ships = 0

        for r in range(nrows):
            horz_ship_len = 0
            for c in range(ncols):
                if board[r][c] == 'X':
                    horz_ship_len += 1
                else:
                    if horz_ship_len == 1:
                        if r == nrows - 1 or board[r+1][c-1] == '.':
                            # have to count the ship now.  it doesn't extend past this row
                            num_ships += 1
                    elif horz_ship_len > 1:
                        num_ships += 1
                    horz_ship_len = 0
            if horz_ship_len != 0 and (r == nrows - 1 or board[r+1][ncols - 1] == '.'):
                num_ships += 1

        return num_ships

