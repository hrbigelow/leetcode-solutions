"""
There are a row of n houses, each house can be painted with one of the k
colors. The cost of painting each house with a certain color is different. You
have to paint all the houses such that no two adjacent houses have the same
color.

The cost of painting each house with a certain color is represented by an n x k
cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2, and so on...

Return the minimum cost to paint all houses.

"""

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
