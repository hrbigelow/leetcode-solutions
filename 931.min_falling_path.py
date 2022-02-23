class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        pre = [float('inf')] + [0] * n + [float('inf')]
        dp = pre.copy()
        
        for i in range(m):
            for j in range(n):
                d = j+1
                dp[d] = min(pre[d-1], pre[d], pre[d+1]) + matrix[i][j]
            pre[:] = dp

        return min(dp)
    
"""
Define the DP matrix with padding on top and both sides.  The top should
be all zeros, the two sides inf.

Took 3 tries.

The mistake centered around dp[0] and dp[-1] being None and never being updated,
so pre[0] and pre[-1] were None in later iterations, when they should have been inf.
"""
