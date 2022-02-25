class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if len(s3) != n+m:
            return False
        
        dp = [[None] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(n):
            dp[i+1][0] = dp[i][0] and s1[i] == s3[i]
            
        # for i in range(1, n+1):
        #     dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(m):
            dp[0][j+1] = dp[0][j] and s2[j] == s3[j]
            
        # for j in range(1, m+1):
        #     dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = (
                    (dp[i][j+1] and s1[i] == s3[i+j+1]) or
                    (dp[i+1][j] and s2[j] == s3[i+j+1])
                )
                
        
        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         dp[i][j] = (
        #             (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or
        #             (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        #         )
        
        return dp[-1][-1]
        
"""
Solved in 22 minutes.  

My first thought was to do a 2 x len(s3) DP array, but I quickly realized that that was not sufficient.

I made an indexing error.  There are two indexing styles, shown above.  First one is centric to the
dp array.  Second one to the value arrays.  The second style is a bit simpler in this case.


Each character of s3 must be assigned to either s1 or s2.  So, the DP state is 2 x n,
where n = len(s3)

If we can get to the end of s3 and the lengths check out, it means yes

But, this isn't the only thing we need to keep track of.  The possible paths go through
an n x m matrix.

"""
