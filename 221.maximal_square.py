"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        
        pre = [0] * (C+1)
        dp = [0] * (C+1)
        m = 0
        
        for i in range(R):
            for j in range(1, C+1):
                if matrix[i][j-1] == "0":
                    dp[j] = 0
                else:
                    dp[j] = 1 + min(dp[j-1], pre[j-1], pre[j])
            pre[:] = dp
            m = max(m, max(dp))
            
            print(dp)
        
        return m**2
        
        
"""
I came up with a solution, after one dead end.  The trick was to use the fact that
we are specifically looking for squares.  I noticed that, if I knew the sizes of the
maximum squares whose lower right corner ended just above, just to the left, and above and left
of a cell, then the production rule was simple.

dp[0][j] = 0
dp[i][0] = 0
dp[i+1][j+1] = size of maximum square with lower right corner at i,j


"""
