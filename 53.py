"""
Dynamic Programming:

The max subarray must end at one of the positions 0 through n-1.
If we compute the max subarray ending at position i, we know that the
max subarray ending at position i+1 must be either the extension of the
one ending at i, or simply nums[i+1].
"""
class Solution:
        
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')]
        for el in nums:
            dp.append(max(dp[-1] + el, el))
        return max(dp)
