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
19 min: first draft
25 min: realized dfs may cause stack overflow, trying anyway
29 min: finished

"""
