"""

You are given a string s and an integer k, a k duplicate removal consists of
choosing k adjacent and equal letters from s and removing them, causing the
left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is
guaranteed that the answer is unique.

"""

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
