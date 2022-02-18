class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # return true if digit d would break the Sudoku rules
        # if placed at position i, j
        def conflict(i, j, d):
            for c in range(9):
                if board[i][c] == d:
                    return True
            for r in range(9):
                if board[r][j] == d:
                    return True
            
            s = i - (i % 3)
            t = j - (j % 3)
            for r in range(s, s + 3):
                for c in range(t, t + 3):
                    if board[r][c] == d:
                        return True
            
            return False
        
        def nextpos(i, j):
            m = i * 9 + j
            m += 1
                            
            while m != 81 and board[m//9][m%9] != '.':
                m += 1
            return m//9, m % 9
            
        
        # all cell positions before i, j have been filled out to
        # some value and do not conflict.  after the call, 
        
        def backtrack(i, j):
            if i == 9:
                return True
            
            ni, nj = nextpos(i, j)
            for d in '123456789':
                if conflict(i, j, d):
                    continue
                board[i][j] = d
                if backtrack(ni, nj):
                    return True
                
                board[i][j] = '.'
            
            return False # board was unsolvable
                
        backtrack(*nextpos(0, -1))
        
            
"""
I had the basic idea of this and mostly implemented in 15 minutes.  Then, it took 2 hours to
debug.  I did not appreciate the termination condition, and also, how to handle the recursive call



"""
