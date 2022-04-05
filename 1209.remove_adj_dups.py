class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        chs = [] # character
        cts = [] # count
        
        for ch in s:
            if not chs or chs[-1] != ch:
                chs.append(ch)
                cts.append(1)
            else:
                cts[-1] += 1
            if cts[-1] == k:
                chs.pop()
                cts.pop()
        
        return ''.join(ch * ct for ch, ct in zip(chs, cts))
        
        
        
"""
Solved in 12 minutes.  Was a bit stuck at the beginning, but
realized that the stack-based method of keeping track of counts was
a sound method, not requiring any separate searching.
"""
