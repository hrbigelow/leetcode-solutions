class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [[0] * 4 for _ in range(n)]
        dp[0][:] = list(costs) + [float('inf')]

        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i-1]) + costs[j]

            # scan backwards for qualifying days
            min_week, min_month = float('inf'), float('inf')
            p = i-1
            while p != -1:
                if days[p] + 7 > days[i]:
                    min_week = min(min_week, dp[p][1])
                if days[p] + 30 > days[i]:
                    min_month = min(min_month, dp[p][2])
                else:
                    break
                p -= 1
                
            dp[i][3] = min(min_week, min_month)
                
        return min(dp[-1])
        
"""
Took 45 minutes.  My first concept of the DP was wrong, since I was only looking through the previous
state, which wasn't guaranteed to be the relevant state that could cover a non-purchase.

I correctly noticed that one can index over *travel days* rather that all 365 days.

I mistakenly wanted to add the previous cost to the non-purchase state.


Let j==3 signify a non-purchase

dp[i][j] # min cost to be covered up to and including travel day i, with purchase type j on
         # travel day i.  Or, inf if the travel is not covered.
         
dp[0][3] = 'inf'.  We must buy something on the zero-th travel day
dp[0][<3] = *costs

No, this doesn't work because we need to look back further than the previous purchase

Instead of 

My first attempt: (erroneous)

For i > 0:
dp[i][3] = min(dp[i-1][1] + costs[1] if days[i-1] + 7 >= days[i] else float('inf'),
               dp[i-1][2] + costs[2] if days[i-1] + 30 >= days[i] else float('inf'))

dp[i][0] = min(dp[i-1]) + costs[0]
dp[i][1] = min(dp[i-1]) + costs[1]
dp[i][2] = min(dp[i-1]) + costs[2]

"""
