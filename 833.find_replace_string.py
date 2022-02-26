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
