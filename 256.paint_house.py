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
