"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are
divided into n and m non-empty substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1

The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3
+ s3 + ...

Note: a + b is the concatenation of strings a and b.

"""

"""
What are the mutually exclusive categories?

The last element in the progressive building of s3 can be either from s1 or s2.

I'm not sure, but this may be one of those DP algorithms that isn't amenable
to a moving-window DP array.  In such a situation, perhaps memoizing is better.


"""

# 40 ms
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for __ in range(len(s2) + 1)] for __ in range(len(s1) + 1)]
        dp[0][0] = True
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
            for j in range(1, len(s2) + 1):
                dp[i][j] = (
                    (dp[i-1][j] and s1[i-1] == s3[i-1 + j]) or
                    (dp[i][j-1] and s2[j-1] == s3[i + j-1])
                )

        return dp[-1][-1]


# 20 ms
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        
        memo = {}
        def recurse(i, j):
            if (i, j) not in memo:
                memo[(i, j)] = (
                    i + j == len(s3) or
                    i < len(s1) and s1[i] == s3[i + j] and recurse(i + 1, j) or
                    j < len(s2) and s2[j] == s3[i + j] and recurse(i, j + 1)
                )
            
            return memo[(i, j)]
        
        return recurse(0, 0)

