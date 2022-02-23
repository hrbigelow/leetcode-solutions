class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for v in coins:
            for a in range(amount+1-v):
                dp[a+v] += dp[a]
        
        return dp[amount]
        
"""
Got this after a lot of thought.

How about this:

process each coin one at a time.  For each coin and each amount,
add dp[a+v] += dp[a]

Let dp[c][a] represent the number of ways you can achieve amount a using coins[:c+1]

If v = coins[c]
dp[c][a+v] = dp[c-1][a+v] + dp[c][a]

This is conveniently calculated in a cumulative forward fashion.

"""
