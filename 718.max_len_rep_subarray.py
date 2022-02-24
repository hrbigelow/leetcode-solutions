class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [0] * (n1 + 1)
        max_sub = 0
        for q in nums1:
            for j in reversed(range(n2)):
                d = j+1
                if q != nums2[j]:
                    dp[d] = 0
                else:
                    dp[d] = dp[d-1] + 1
            max_sub = max(max_sub, max(dp))
        
        return max_sub
      
"""
Solved in 13 minutes.  Made the mistake that I forgot the whole
dp array (2D) was needed for the answer, not just the last row.

Lesson:  There is a distinction between being able to throw out
unneeded dp cells during the dp calculation, and whether the
answer will exist in a subset of dp cells or among all of them.

"""
