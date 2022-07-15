"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

"""

"""
Dynamic Programming:

The max subarray must end at one of the positions 0 through n-1.
If we compute the max subarray ending at position i, we know that the
max subarray ending at position i+1 must be either the extension of the
one ending at i, or simply nums[i+1].

Why?  Because the max subarray that can be formed which ends at position i
either does or does not include elements before i.  If it does, then it
should include the max subarray in order to maximize itself.

Turns out this is Kadane's Algorithm
"""
class Solution:
        
    def maxSubArray(self, nums: List[int]) -> int:
        dp = float('-inf')
        m = float('-inf')
        for el in nums:
            dp = max(dp + el, el)
            m = max(m, dp)
        return m
