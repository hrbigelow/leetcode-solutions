"""
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

"""

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
