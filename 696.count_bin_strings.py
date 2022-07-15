"""
Given a binary string s, return the number of non-empty substrings that have
the same number of 0's and 1's, and all the 0's and all the 1's in these
substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they
occur.

"""
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
