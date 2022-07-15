"""
Given a string s, find the length of the longest substring without repeating
characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        starts = {}
        max_len = 0
        length = 0
        beg = 0
        for i, ch in enumerate(s):
            if ch in starts and starts[ch] >= beg:
                beg = starts[ch] + 1
                length = i - beg
            starts[ch] = i
                    
            length += 1
            max_len = max(max_len, length)
        
        return max_len
    
        
"""
Finished in 19 minutes.  At first I thought I could do it just with a simple hash,
but it turned out I needed to maintain a start position as well.

1. maintain m, a maximum length
2. 

"""
