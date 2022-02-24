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
