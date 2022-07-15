"""
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)
        while lo != hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                # mid is an upper bound, eliminate upper bounds beyond this
                hi = mid

        beg = lo

        # beg is a least upper bound of target
        
        # search for least upper bound in [lo, end)]
        lo, hi = beg, len(nums)
        while lo != hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target + 1:
                lo = mid + 1
            else:
                hi = mid

        # least upper bound of target + 1
        end = lo
        
        if beg == end:
            return [-1, -1]
        
        else:
            return [beg, end-1]
        
"""
5 min: first draft
13 min: finished

Really need to get straight what least upper bound, greatest lower bound, and equal range
really are.  This has always confused me.
"""
