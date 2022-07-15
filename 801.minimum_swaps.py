"""
You are given two integer arrays of the same length nums1 and nums2. In one
operation, you are allowed to swap nums1[i] with nums2[i].

For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the
element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].

Return the minimum number of needed operations to make nums1 and nums2 strictly
increasing. The test cases are generated so that the given input always makes
it possible.

An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] <
... < arr[arr.length - 1].

"""

class Solution:
    def minSwap(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        dp = [[0,0] for _ in range(n)]
        dp[0][1] = 1
        for i in range(1, n):
            same_good = a[i-1] < a[i] and b[i-1] < b[i]
            cross_good = b[i-1] < a[i] and a[i-1] < b[i]
            
            dp[i][0] = min(
                dp[i-1][0] if same_good else float('inf'), 
                dp[i-1][1] if cross_good else float('inf')
            )
               
            dp[i][1] = min(
                dp[i-1][0] if cross_good else float('inf'),
                dp[i-1][1] if same_good else float('inf')
            ) + 1

        return min(dp[-1][0], dp[-1][1])
    
"""
It seems like this should work.  No, the dp state needs also to include the top and bottom values, but
that 

dp[i][0] indicates the best qualifying set of swaps of a[:i+1] and b[:i+1] which ends with no swap at position i.
dp[i][1] is the same but ends with the swap at position i.



"""
