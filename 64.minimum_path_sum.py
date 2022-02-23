class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        
        for i in range(m):
            for j in range(n):
                dp[j+1] = min(dp[j], dp[j+1]) + grid[i][j]
        
        return dp[-1]
        
        
        
"""
Setting dp[0] = inf allows ignoring the non-existent left neighbor for the
left-most cells.

Setting dp[1] = 0 allows entering the graph from above at the first column

Setting dp[>1] = inf disallows entering the graph from above, after the first column

The proper way to visualize this is to imagine the augmented maze.  It is still tricky.
"""
