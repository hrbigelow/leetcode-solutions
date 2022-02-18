class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre = '$'
        p, q = 0, 0
        ct = 0
        for c in s:
            if c != pre:
                ct += min(p, q)
                p, q = q, 0
            pre = c
            q += 1

        ct += min(p, q)
        return ct

"""
Solved in 10 minutes.  First attempt used indices unnecessarily rather than simple
increment with direct runlengths

"""
