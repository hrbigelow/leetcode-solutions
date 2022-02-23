class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        m = len(og)
        n = len(og[0])
        
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(1, n+1):
                if og[i][j-1] == 0:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = 0
            dp[0] = 0
        
        return dp[-1]
        
        
"""
This is the same recurrence except will be 0 where there is an obstacle.

"""
