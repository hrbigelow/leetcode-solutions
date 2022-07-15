"""
Given a string s, return the lexicographically smallest subsequence of s that
contains all the distinct characters of s exactly once.

"""

"""
Intuition:
Do in a single pass over the text
At any moment, you know how many of each letter are left, using cnt array

At all times, the stack represents the best string we have
among the input processed so far.  It is maintained based on two principles:

1. Base case: stack is empty, no input has been consumed
2. stack contains the best string so far, we have a next character
   1. If the character has been seen before, do not alter the stack
   2. Otherwise, pop elements off the stack if the element character:
      a: still exists in the input
      b: is greater than this character
      
      Step a ensures that you can still complete the stack by the end of the input
      Step b replaces the suffix of the stack with a lower character
      
The seen dictionary ensures that we only add each character once.


Overall Ideas

Loop invariant maintains the answer in the stack for the input
seen.

This is similar to 
"""

class Solution:
    def smallestSubsequence(self, S):
        cnt = collections.Counter(S)
        seen = dict.fromkeys(S)
        stk = ['']
        for c in S:
            if not seen[c]:
            while stk[-1] > c and cnt[stk[-1]]:
                seen[stk.pop()] = 0
            seen[c] = 1
            stk.append(c)
            cnt[c] -= 1

        return ''.join(stk)
    
