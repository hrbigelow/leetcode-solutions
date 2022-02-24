class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        
        pre = costs[0]
        cur = [None] * k
        
        for cols in costs[1:]:
            
            y = None
            min1, min2 = float('inf'), float('inf')
            for i, p in enumerate(pre):
                if p < min1:
                    y, min1 = i, p

            for i, p in enumerate(pre):
                if i != y and p < min2:
                    min2 = p
                    
            for j in range(k):
                cur[j] = (min1 if j != y else min2) + cols[j]
            pre[:] = cur
        
        return min(pre)
    
            
        
        
"""
Solved in 5 minutes, no mistakes (except switched index and value for the enumerate clause)

How to efficiently get the minimum of all round robin omissions?

1. do O(k) scan to find indices for min y and second-min z
2. construct array mins = [min] * k, then set mins[y] = second_min

I thought of this only after reading the solution.  But, it is easy enough to understand.
The loop for finding the min and second min is hard to do in one pass.

"""
