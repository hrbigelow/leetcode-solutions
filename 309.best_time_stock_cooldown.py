"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements. For
example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold, hot, cool = 0, 1, 2
        dp = [[-float('inf')] * 3 for _ in range(n+1)]
        dp[0][cool] = 0
        
        for d in range(1, n+1):
            dp[d][hold] = max(dp[d-1][hold], dp[d-1][cool] - prices[d-1])
            dp[d][hot] = dp[d-1][hold] + prices[d-1]
            dp[d][cool] = max(dp[d-1][hot], dp[d-1][cool])
        
        return max(dp[-1][hot], dp[-1][cool])
    
"""
Wow!  I got this on the first try.  I think that the key in this question was
to correctly identify all possible *states* of the system, and then the transition
diagram is straightforward.
"""
