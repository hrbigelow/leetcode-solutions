"""
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo != hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        return lo if nums[lo] == target else -1
    
    

"""
Solved in 4 minutes

Is the [lo, hi] interval guaranteed to shrink at every iteration?
Yes, because mid != hi when lo != hi, and mid != lo + 1.
"""
