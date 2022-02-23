class Solution:
    def numDecodings(self, s: str) -> int:
        digits = set(str(i) for i in range(1, 27))
        n = len(s)
        a = 1                           # dp[0]
        b = 0
        # b = 1 if s[0] in digits else 0  # dp[1]
        c = 0

        pch = '-'
        for ch in s:
            c = 0
            if ch in digits:
                c += b
            
            if pch+ch in digits:
                c += a
                
            pch = ch
            a, b = b, c
            
        return b
    
        """
        for i in range(2, n + 1):
            c = 0
            if s[i-2:i] in digits:
                c += a

            if s[i-1] in digits:
                c += b
                
            a, b = b, c
        
        return b        
        """
        
        
        
"""
This took 45 minutes.  The basic idea was there, but I made several indexing mistakes.
First I got confused between the dp index and the array indices.  Still not sure the
best way to handle that.

Want to return dp[n], number of ways to decode s[:n]
The loop calculates dp[i], then 

i is the dp index
a is dp[0], the number of ways you can decode the empty string.  this should be 1
b is dp[1]

The base case is tricky.  The number of ways you can decode the empty string should be 1,
because if you have a single valid digit, it is an extension of the base case.

with two digits, it is a two-digit extension of the base case, plus a one digit extension
of the one-digit base case.

Refinement:

We want to do one extension for each element of s[1:]

Is it possible to do this with a sentinel value?

"""
