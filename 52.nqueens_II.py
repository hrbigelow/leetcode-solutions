"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens
puzzle.

"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        def advance(mask):
            new_mask = [0] * n
            for i in range(n):
                new_mask[i] |= mask[i] & 1 # vertical
            for i in range(n-1):
                new_mask[i] |= mask[i+1] & 2 # right-to-left
            for i in range(1, n):
                new_mask[i] |= mask[i-1] & 4 # left-to-right
                
            return new_mask

        def backtrack(row, count, mask):
            # precondition:
            # count reflects the number of ways that
            if row == n: return count + 1
            mask = advance(mask)
            for col, m in enumerate(mask):
                if m != 0:
                    continue
                mask[col] = 7
                count = backtrack(row+1, count, mask)
                mask[col] = m
            return count
        
        mask = [0] * n
        return backtrack(0, 0, mask)
                
"""
In plain English:

we go down the chess board row by row.  At the first call, the count is zero
and the mask is blank, indicating that a queen *could* be placed anywhere in
the previous row and not threaten previous queens.  We advance the mask to row zero.

Then, for each free square in row zero, we place a queen, create a new mask to reflect
the state of row zero, then call backtrack on the next row with the new mask

backtrack is called at a particular row with a particular mask.  The count is 

"""
