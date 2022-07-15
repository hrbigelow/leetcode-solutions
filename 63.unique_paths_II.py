"""
You are given an m x n integer array grid. There is a robot initially located
at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down
or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that
the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2
* 109.

"""

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
