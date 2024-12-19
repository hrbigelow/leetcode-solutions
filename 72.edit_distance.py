"""
Why does this work?

First, note that we are viewing this problem not as "editing the first string to match the second",
but as:

editing two strings (starting from two empty strings) to match the prefixes of each string,
and along the way, recording the penalty incurred

If you wanted to record parent pointers, then you could also get a set of edits.  It's not clear exactly
whether the edits can be in any order or not.

Memory optimization:

The lookback only goes vertically up, horizontally, or

Induction:
If you know dp[i-1][j], dp[i][j-1] and dp[i-1][j-1], then you know that dp[i][j]
is constructed either by:
1. extending each string by one, and adding a match/mismatch 0/1 penalty
2. adding a character to the first string

"""

class Solution:
    def minDistance(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)
        dp = list(range(nb+1))
        tmp = [None] * (nb+1)
        for i in range(na):
            pre = dp[0] + 1
            for j in range(1, nb + 1):
                cur = min(dp[j] + 1, pre + 1, dp[j-1] + 1 - (a[i] == b[j-1]))
                dp[j-1] = pre
                pre = cur
            dp[-1] = pre
            # dp = list(tmp)
        
        return dp[-1]
