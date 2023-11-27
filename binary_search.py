import math

"""
target = 5
nums:   1 2 3 4 5 5 5 6 7 8
lt  :   T T T T                   round-down compatible
ge  :           T T T T T T       round-down compatible
lb  :           ^

lt2 :   T T T T T                 round-up compatible
ge2 :             T T T T T       round-up compatible
lb  :           ^

le  :   T T T T T T T             round-down compatible
gt  :                 T T T       round-down compatible
ub  :                 ^

"""

def lower_bound(nums, target):
    # Return lowest insertion point for target
    lo, hi = 0, len(nums)
    while lo != hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo

def upper_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo != hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo


target = 5
nums = [1,2,3,4,5,6,7,8]

lb = lower_bound(nums, target)
ub = upper_bound(nums, target)

print(f'nums[{lb=}:{ub=}]={nums[lb:ub]}')

