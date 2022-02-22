class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        st = [0]
        dead = set()
        while st:
            pos = st.pop()
            dead.add(pos)
            for w in wordDict:
                end = pos+len(w)
                if s[pos:end] != w:
                    continue
                if end == n:
                    return True
                if end not in dead:
                    st.append(end)
        return False

"""
This is an explicit-stack depth-first search solution using caching.

"""

class Solution:

    def wordBreak(self, s: str, wd: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n+1):
            dp[i] = any(dp[i-len(w)] and s[i-len(w):i] == w for w in wd if i >= len(w))

        return dp[-1]

"""
This DP solution is conceptually very clean:

1. Break up s into its n+1 prefixes, s[:0], s[:1], ..., s[:n]
2. Assume dp[i] = feasibility of segmenting s[:i]
3. Let dp[i] = any(dp[i-len(w)] and s[i-len(w):i] == w for w in wd if i >= len(w))
"""

