"""
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""

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
