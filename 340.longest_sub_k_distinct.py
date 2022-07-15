"""
Given a string s and an integer k, return the length of the longest substring
of s that contains at most k distinct characters.
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        
        m, i, j = 0, 0, 0
        n = len(s)
        rb = dict()
        
        while j != n:
            if len(rb) < k or s[j] in rb:
                rb[s[j]] = j
                j += 1
                m = max(m, j - i)
            else:
                if s[i] in rb and rb[s[i]] == i:
                    del rb[s[i]]
                i += 1
        
        return m
    
"""
NOTES:

The main loop maintains a pair of positions i, j, such that s[i:j] never contains more than k
distinct characters.  The loop greedily either increments j if it wouldn't violate the k constraint,
otherwise it increments i.  Every time it increments j, it updates m, the maximal interval found.
rb contains character keys, the value being the position of the right-most occurrence of that character
within s[i:j].  It does a double-duty.  First, the length of rb says how many distinct characters are in s[i:j],
and second, it is easy to check that the occurrences of such a character exit the range s[i:j] when i is
incremented, just by the test rb[s[i]] == i.

"""
