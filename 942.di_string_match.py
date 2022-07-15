"""
A permutation perm of n + 1 integers of all the integers in the range [0, n]
can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are
multiple valid permutations perm, return any of them.

"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo, hi = 0, len(s)
        res = []
        for c in s:
            if c == 'I':
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        
        res.append(lo)
        return res
        
"""
After noticing that a recursive decomposition is possible, note that
this can be done iteratively.  Any given pattern can be decomposed by
just one character, and the rest.  The one character being an I means the first
value could be the lowest value and not interfere with the answer for the remaining
part.

Similarly, if the first character is 'D', then the first value could be the highest value,
and the remaining values could be used without any conflict

"""
