class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [1]
        for n in nums[:-1]:
            fwd.append(fwd[-1] * n)
            
        rev = [1]
        for n in reversed(nums[1:]):
            rev.append(rev[-1] * n)
        
        rev.reverse()
        
        return [f * r for f, r in zip(fwd, rev)]
    
        
"""
Without division, need two running product arrays

fwd[i] = prod(nums[:i])
rev[i] = prod(nums[i+1:])


Solved in 9 minutes, three attempts

First attempt I thought using rev = reversed(rev) instead of rev.reverse() was a problem.
Then, I realized that I was populating fwd and rev incorrectly with the whole array instead of
with nums[:-1] and nums[1:], respectively.
"""
