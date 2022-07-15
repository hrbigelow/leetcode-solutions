"""
There is a row of n houses, where each house can be painted one of three
colors: red, blue, or green. The cost of painting each house with a certain
color is different. You have to paint all the houses such that no two adjacent
houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3
cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.

"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        pre = costs[0]
        cur = [None] * 3
        
        for i in range(1, n):
            cur[0] = min(pre[1], pre[2]) + costs[i][0]
            cur[1] = min(pre[0], pre[2]) + costs[i][1]
            cur[2] = min(pre[0], pre[1]) + costs[i][2]
            pre[:] = cur
        
        return min(pre)
        
"""
Finished in 8 minutes.  First submission failed due to None in cur.
Edge case is when n == 1 and the loop didn't execute.

Fix was to return min(pre) rather than min(cur).

I think the states are just dp[i][j]

i: house
j: color

dp[0] = { *costs[0] }
dp[i][red] = min(dp[i-1][green], dp[i-1][blue]) + costs[i][red]
etc

Since this is just 

"""
