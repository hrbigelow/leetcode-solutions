"""

There are n children standing in a line. Each child is assigned a rating value
given in the integer array ratings.

You are giving candies to these children subjected to the following
requirements:

Each child must have at least one candy.

Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies
to the children.

"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [None] * len(ratings)
        
        # precondition:  assume candy can only be added
        def rec(beg, end, min_left, min_right):
            if end == beg:
                candy[beg] = max(min_left, min_right)
                return
            
            mid = beg + (end - beg) // 2
            if ratings[mid] < ratings[mid+1]:
                rec(beg, mid, min_left, 1)
                rec(mid+1, end, candy[mid] + 1, min_right)
                
            elif ratings[mid] > ratings[mid+1]:
                rec(mid+1, end, 1, min_right)
                rec(beg, mid, min_left, candy[mid+1] + 1)
            
            else:
                rec(beg, mid, min_left, 1)
                rec(mid+1, end, 1, min_right)
        
        rec(0, len(ratings) - 1, 1, 1)
        return sum(candy)
    
                
        
        
"""
22 min: first draft
36 min: finished

The two-pass approach is much simpler and less memory.
"""
