"""
You are given an integer array nums. You want to maximize the number of points
you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
delete every element equal to nums[i] - 1 and every element equal to nums[i] +
1.

Return the maximum number of points you can earn by applying the above
operation some number of times.

"""

class Solution:
    from collections import Counter
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        pre_take, pre_leave = 0, 0
        pre_val = -1
        for v in sorted(c.keys()):
            cur_take = v * c[v] + max(pre_take if pre_val + 1 < v else 0, pre_leave)
            cur_leave = max(pre_take, pre_leave)
            pre_take, pre_leave = cur_take, cur_leave
            pre_val = v
            
        return max(cur_take, cur_leave)
            
        
"""
Solved in 20 minutes

Order doesn't matter, just the histogram of counts, and if we sort them by order,

For each distinct value, we could either take, or not take it.  Record the value if we take or not
take it.  So, let's say there are k distinct numbers, then we have 2k choices.

dp[i+1]['take'] = v[i+1] * c + max(dp[i]['take'] if nums[i] + 1 < nums[i+1] else 0, dp[i]['leave'])
dp[i+1]['leave'] = max(dp[i]['take'], dp[i]['leave'])


"""
