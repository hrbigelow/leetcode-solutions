"""
Given an integer array nums sorted in non-decreasing order, return an array of
the squares of each number sorted in non-decreasing order.

"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        results = []
        st = []
        for n in nums + [float('inf')]:
            sq = n**2
            while st and st[-1] < sq:
                results.append(st.pop())
            st.append(sq)
                
        return results
    
        
"""
Solved in 9 minutes.

I had the stack idea in the first minute, but it was tricky to
work out the details.

My first attempt had a separate step that appended the left over elememts of the stack
in reverse.  Using the sentinel value is cleaner
I wanted to do this in one pass, O(N).

"""
