"""
Given a string s, return true if the s can be palindrome after deleting at most
one character from it.

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1

        for k, l in ((i+1, j), (i, j-1)):
            while k < l:
                if s[k] != s[l]:
                    break
                k += 1
                l -= 1
            if k >= l: return True
        
        return False

"""
This is a progressive solution which I think somewhat directly expresses the basic idea of
a palindrome with an optional skip.  The first part advances both boundaries as far as it can,
while the second part attempts from two starting points.  The first skips the lower boundary ahead one,
while the second skips the upper boundary.

"""
