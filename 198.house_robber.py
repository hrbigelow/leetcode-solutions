class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b, c = 0, 0, 0
        for i in range(len(nums)):
            c = max(a + nums[i], b)
            a, b = b, c
        
        return c
    
"""
The space of all possible problems is a 2^N set of combinations
of houses robbed.  Breaking it down into progressive choices, we have
a choice to rob or not rob house i.  Then, just using the faith-based
approach of assuming you have the right answer for i houses and ask:
How can I construct the answer for the i'th (zero based) house given these
previous answers?

Note that it is convenient to prepend two dummy houses with zero wealth
so that we don't need any branches.


dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
dp[i] = max(dp[i-1], nums[i] + dp[i-2])

"""
