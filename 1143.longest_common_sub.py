class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)
        pre = [0] * (nb + 1)
        dp = [0] * (nb + 1)
        for i in range(na):
            for j in range(1, nb + 1):
                dp[j] = max(pre[j-1] + int(a[i] == b[j-1]), dp[j-1], pre[j])
            pre[:] = dp
                
        return dp[-1]
    
        
        
"""
This took awhile to work out the right DP recurrence.  A few things to note:
The DP state space was the combination of every possible pair of prefixes of a or b.
Note that for an array of n elements, there are n+1 subarray prefixes, the empty subarray
being the shortest.

So, the virtual DP matrix is (na+1) x (nb+1)

The next challenge was noticing that there are three ways to calculate a given state:

dp[i][j] = max(dp[i-1][j-1] + int(a[i-1] == b[j-1]), dp[i-1][j], dp[i][j-1])

"""

