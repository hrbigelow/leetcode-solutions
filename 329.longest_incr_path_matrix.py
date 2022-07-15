"""
Given an m x n integers matrix, return the length of the longest increasing
path in matrix.

From each cell, you can either move in four directions: left, right, up, or
down. You may not move diagonally or move outside the boundary (i.e.,
wrap-around is not allowed).

"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        from collections import deque
        
        nr = len(matrix)
        nc = len(matrix[0])
        
        lplen = [[None] * nc for _ in range(nr)]

        def dfs(i, j):
            if lplen[i][j] is not None:
                return lplen[i][j]

            suffix_length = 0

            for next_i, next_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if not (0 <= next_i < nr and 0 <= next_j < nc):
                    continue

                if matrix[i][j] >= matrix[next_i][next_j]:
                    continue

                suffix_length = max(suffix_length, dfs(next_i, next_j))

            lplen[i][j] = suffix_length + 1

            return lplen[i][j]
        
        for i in range(nr):
            for j in range(nc):
                _ = dfs(i, j)
                
        return max(el for row in lplen for el in row)
    
"""
First thought this would not be memo-izable, because the longest path starting from
any particular position might not be the same if it were a continuation of two different
paths.  Also I was thinking about the 'visited' array, and realized you don't actually need it!
Since the paths must be strictly increasing, there is no possibility of cycles.

This then lead to realizing that prefixes don't interfere with the longest path starting at
a given point, therefore the whole thing was cacheable.

I then wrote a dfs with memoization.  However, since the matrix was possibly 200 x 200 I worried
that there could be stack overflow.  I tried it and it succeeded anyway.  I briefly tried BFS, but
realized that is difficult to implement since one needs to *return* the length rather than pass it
down.

It is of course possible to do an explicit stack dfs, but that is pretty hard.


19 min: first draft
25 min: realized dfs may cause stack overflow, trying anyway
29 min: finished

"""
