"""

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work
on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job
schedule is the sum of difficulties of each day of the d days. The difficulty
of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty
of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule
for the jobs return -1.
"""

class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        n = len(jd)
        dp = [[0] * n for _ in range(d)]
        dp[-1][-1] = -1
        max_diff = 0
        for j in range(n):
            max_diff = max(max_diff, jd[j])
            dp[0][j] = max_diff
        
        accu = [0] * n
        for i in range(1, d):
            for j in range(i, n):
                accu[j] = jd[j]
                for a in reversed(range(i, j)):
                    accu[a] = max(accu[a+1], jd[a])

                # accu[k] == max(jd[k:j+1])
                # j is used as an index in the dp, and as a limit in both ranges
                dp[i][j] = min(dp[i-1][k-1] + accu[k] for k in range(i, j+1))
                
        return dp[-1][-1]
        
"""
Took an hour.  One of the difficulties is in using j both for an index
for the dp array and a limit for a range.  When used as a limit, one should use
j+1.

n: number of jobs
d: number of days

let dp[i][j] be the total difficulty after completing j+1 jobs in i+1 days

dp[0][j] = max(jd[:j+1])
dp[i>0][j>=i] = min(dp[i-1][k] + max(jd[k+1:j+1]) for k in range(j))

Answer is dp[d-1][n-1]

How to compute a set of max'es

Note that the expression uses a nested loop, and in both cases, the range uses j as a limit.

We want to compute the max of the range k:j+1 for a set of ranges.  Most efficient would be
to populate an array of such maxes backwards.  This would be order 
"""
