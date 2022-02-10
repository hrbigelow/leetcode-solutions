from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        return ''.join(ch * ct for ch, ct in sorted(ctr.items(), key=lambda p: -p[1]))
    
    
"""
Completed in 2 minutes
"""
