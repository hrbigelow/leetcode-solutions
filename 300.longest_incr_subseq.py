class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            dp[i] = 1 + max(dp[j] if nums[j] < nums[i] else 0 for j in range(i))
            
        
        return max(dp)
        
        
"""
Define dp[i] as length of LIS of nums[:i+1] whose last element is nums[i], or 0 if not possible

In this case, I returned dp[-1] rather than max(dp).  Must remember that dp may contain a subcase of
the answer.  In this case, it is the length of the LIS *which happens to end at nums[i]*



dp[0] = 1
dp[i>0] = 1 + max(dp[j] if nums[j] < nums[i] else 0 for j in range(i))

At each iteration i, you are searching for a maximal value of a filtered value.

The values are (dp[j], nums[j]).  Suppose you sort by nums[j] descending, then by dp[j]
descending.  Then you can perform a binary search to find the point where nums[j] < nums[i],
then take the first element there.

The official solution uses a different approach, quite heuristic
"""
