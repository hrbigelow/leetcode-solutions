class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        start = ord('a')
        for c in s:
            counts[ord(c) - start] += 1
        for c in t:
            counts[ord(c) - start] -= 1
            
        return all(c == 0 for c in counts)
        
        
"""
4 min: first draft (finished)
"""
