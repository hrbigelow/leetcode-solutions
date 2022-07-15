"""
Given a string s, sort it in decreasing order based on the frequency of the
characters. The frequency of a character is the number of times it appears in
the string.

Return the sorted string. If there are multiple answers, return any of them.

"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        return ''.join(ch * ct for ch, ct in sorted(ctr.items(), key=lambda p: -p[1]))
    
    
"""
Completed in 2 minutes
"""
