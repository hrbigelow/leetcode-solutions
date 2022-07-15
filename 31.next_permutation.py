"""
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of
arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically
greater permutation of its integer. More formally, if all the permutations of
the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in
the sorted container. If such arrangement is not possible, the array must be
rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].

While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

"""

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
