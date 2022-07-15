"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to
get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.

"""

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

The mapping may be expressed using a single dictionary, with the restriction
that no two keys can map to the same value.



"""


# 32 ms (my solution)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        fwd = {}
        used = set()
        for se, te in zip(s, t):
            if se in fwd:
                if te != fwd[se]:
                    return False

            elif se not in fwd and te not in used:
                fwd[se] = te
                used.add(te)
            
            else:
                return False
            
        return True

# 20 ms
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d: 
                if d[s[i]] != t[i]:
                    return False
            elif t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]
        return True

