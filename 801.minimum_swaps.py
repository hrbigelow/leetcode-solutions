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
