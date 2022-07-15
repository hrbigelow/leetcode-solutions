"""

Given an integer array nums, find a contiguous non-empty subarray within the
array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

"""

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    
    def __init__(self):
        self.unused_beg = 0 # beginning of the unused portion of the read4 buf
        self.unused_end = -1 # end of the unused portion of read4 buf.  -1 means uninitialized
        self.buf4 = [None] * 4
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        
        while i != n:
            if self.unused_beg >= self.unused_end:
                self.unused_beg = 0
                self.unused_end = read4(self.buf4)
            
            if self.unused_end == 0:
                break
                
            buf[i] = self.buf4[self.unused_beg]
            self.unused_beg += 1
            i += 1
        
        return i


"""
16 min:  first draft
23 min:  first rewrite  (collapse nested loop to single while loop)
24 min:  first test
25 min:  second run   (realized I misunderstood the problem)
34 min:  test         (split out second while condition into loop body)
35 min:  finished

Is there a way to do a single test in the while loop without any pre-initialization?
"""
