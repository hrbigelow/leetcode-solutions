"""

Given an integer n, your task is to count how many strings of length n can be
formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        pre = [1] * 5
        cur = [0] * 5
        mod = 10**9 + 7
        
        a,e,i,o,u = 0,1,2,3,4
        for _ in range(n-1):
            cur[a] = pre[e] + pre[i] + pre[u]
            cur[e] = pre[a] + pre[i]
            cur[i] = pre[e] + pre[o]
            cur[o] = pre[i]
            cur[u] = pre[i] + pre[o]
            pre = [c % mod for c in cur]
        
        return sum(pre) % mod
"""
Solved on the second try in 11 minutes.  Pretty straight forward
"""
