class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 1 0 0 0 0 0 0 0 ...  # target+1 items, zero'th roll
        # 0 0 0 0 0 0
        # ...
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        modu = 10**9 + 7
        
        for i in range(1, n+1):
            for j in range(1, min(i*k, target) + 1):
            # this works too, but less efficient
            # for j in range(1, target+1):
                dp[i][j] = sum(dp[i-1][j-1-b] for b in range(k) if j > b) % modu
        
        return dp[-1][-1]
        
"""
Solved in 30 minutes.  Kinda horrendous.  I rushed through the construction phase and changed
my mind several times on the basic DP definition.  Then, I got confused which definition was which.

One tricky part is implementing the specific optimization of not iterating through j all the way.

Need a 2D DP, target x number of rolls

dp[i][j] : number of ways after the i'th roll to get value j

dp[i][j] = sum(dp[i-b][j-1] for b in range(1, k+1) if i-b >= 0)

"""
