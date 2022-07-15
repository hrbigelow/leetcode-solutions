"""
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = min(coins)
        max_num_coins = amount // min_coin + 1
        dp = [max_num_coins] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            dp[a] = 1 + min((dp[a-v] for v in coins if a-v >= 0), default=max_num_coins)
        """
        for v in coins:
            for a in range(amount+1):
                if a % v == 0:
                    dp[a] = min(dp[a], a // v)
                elif a > v:
                    dp[a] = min(dp[a - q * v] + q for q in range(a // v + 1))

        """
        print(max_num_coins)
        print('dp[amount]: ', dp[amount])
        return -1 if dp[amount] >= max_num_coins else dp[amount]
    
"""
My first attempt was a mis-reading of the problem.  I thought they were asking for the minimum
number of different *kinds* of coins, not the total coin count.  After that, I tried a confusing
approach by going one coin at a time, calculating for every amount.  This passed 70 or so tests,
but I could never debug it fully.

Then, I realized the better solution was just to treat the amount as the only DP state, and realize that
one can fold the 'coins' into one tight calculation.  There is no reason to hold individual coin calculations
around.

So, you just ask:  If I know the answer for amounts less than a, There are at most C ways I can arrive at
a, and it's just a simple min operation.

"""
