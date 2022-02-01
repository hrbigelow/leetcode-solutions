class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i, j, m = 0, 0, 0
        seen = set()
        while j != n:
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                m = max(m, j - i)
            else:
                seen.remove(s[i])
                i += 1
                
        
        return m
    
"""
If you are able to find the longest substring without repeating characters, which starts at position i,
then, you can do that for all i, and choose the longest among those.
This is because the solution must have *some* start position in [0, n), and you just want to find the
longest among those.

So, starting at position i, it is easy to find the longest substring by extending the right end as much as possible
while there are no repeats.  Suppose then, that we've found such a string s[i:j], where s[j] occurs in s[i:j].

What about the longest starting at i+1?  It is either s[i+1:j] or s[i+1:>j].  To distinguish, if s[i] == s[j],
then 

"""
