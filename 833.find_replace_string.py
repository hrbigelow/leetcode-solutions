"""
You are given a 0-indexed string s that you must perform k replacement
operations on. The replacement operations are given as three 0-indexed parallel
arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original
string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] =
"eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement
operations should not affect the indexing of each other. The testcases will be
generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources =
["ab","bc"] will not be generated because the "ab" and "bc" replacements
overlap.

Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.

"""

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indices)
        sn = len(s)
        si = 0
        result = ''
        inds = sorted(range(n), key=lambda i: indices[i])
        
        for r in inds:
            # copy untouched portion to output
            while si < indices[r]:
                result += s[si]
                si += 1
            # check validity of replacement
            if sources[r] == s[si:si+len(sources[r])]:
                result += targets[r]
                si += len(sources[r])
            
        result += s[si:]
        
        return result
    
        
        
"""
14 min: first draft
18 min: test (confused 'copying from source' with copying from s)
21 min: finished

Some checks:

empty replacements => works

At start of loop, si is at the end of the previous replacement span, whether
applied or not.  

Copy part seems right

Validity check seems right

Final append seems right


1. sort the replacements
2. for each replacement:
   a. copy through of si to output
   b. test the replacement validity
      if valid: append target text
                advance si by length of sources text
      otherwise, append sources text
      
   at end of loop, append 

"""
