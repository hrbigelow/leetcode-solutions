class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)
        e = n-1
        
        for i in range(n - n//2):
            I = e-i
            for j in range(i,e-i):
                J = e-j
                tmp = m[i][j]
                m[i][j] = m[J][i]
                m[J][i] = m[I][J]
                m[I][J] = m[j][I]
                m[j][I] = tmp
        
        return
    

        
"""
Finished in 27 minutes.  Four attempts.

"""
