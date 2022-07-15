"""
Given an input string (s) and a pattern (p), implement wildcard pattern
matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

"""

# my solution: 1120 ms
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for pi in range(len(p) + 1)] for si in range(len(s) + 1)]
        dp[0][0] = True  # empty string matches empty pattern
        
        for pi in range(1, len(p) + 1):
            dp[0][pi] = dp[0][pi-1] and p[pi-1] == '*'  # all '*' pattern matches empty string
            for si in range(1, len(s) + 1):
                dp[si][pi] = (
                    (dp[si-1][pi] and p[pi-1] == '*') or
                    (dp[si][pi-1] and p[pi-1] == '*') or
                    (dp[si-1][pi-1] and p[pi-1] in (s[si-1], '*', '?'))
                )
        
        return dp[-1][-1]


# 25 ms
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        i, j, last_i, last_j = 0, 0, -1, -1
        while i < len(s):
            if j == len(p):
                if last_i < 0: return False
                last_i += 1; i, j = last_i, last_j
            elif p[j] in {s[i], '?'}:
                i += 1; j += 1
            elif p[j] == '*':
                j += 1; last_i, last_j = i, j
            else:
                if last_i < 0: return False
                last_i += 1; i, j = last_i, last_j
        return p[j:] == '*'*(len(p)-j)


# 50 ms
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            return s == ''
        i, j, prev_i, prev_j = 0, 0, -1, -1
        while i < len(s):
            if j < len(p) and p[j] in (s[i], '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                prev_i, prev_j = i, j
                j += 1
            else:
                if prev_i < 0:
                    return False
                prev_i += 1
                i = prev_i
                j = prev_j
        return all(c == '*' for c in p[j:])

