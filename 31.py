class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1: return
        j = n - 1
        while j != 0:
            if nums[j-1] < nums[j]: break
            j -= 1
        
        if j == 0:
            nums.reverse()
            return
        
        k = n - 1
        while nums[k] <= nums[j-1]:
            k -= 1
        
        nums[j-1], nums[k] = nums[k], nums[j-1]
        nums[j:] = sorted(nums[j:])
        return
    
        
        
"""
Approach:

Identify the shortest suffix of nums which has a non-maximal sub-permutation.
This is a suffix which is one element longer than one having a maximal sub-permutation.
A maximal sub-permutation is one in which the digits are all non-increasing.

Then, having identified this shortest suffix with non-maximal sub-permutation, the question is,
how to increment it?  The only choice is to replace the most significant digit with the next higher
available one, and then set the remaining digits to their minimal permutation order (ascending)
"""
