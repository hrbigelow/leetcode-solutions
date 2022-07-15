"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i,
height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0
        lo, hi = 0, len(height) - 1
        while lo != hi:
            ma = max(ma, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return ma
        
"""
I spent 20 minutes but gave up.  Considered different ways to cache
intermediate quantities, and also whether a DP solution would work.  I adapted
my own explanation after seeing the solution:

The total search space is the upper triangle of the i,j matrix (without
diagonal) If we start at the upper right corner, which represents [0, n-1],
then one of two cases is true:

1.  if h[i] < h[j], all intervals to the left hold less water, because any
h[<j] that is higher than h[j] will be limited in height by h[i], but the width
is shrinking.

if h[i] >= h[j], all intervals below will hold less water.

You can see this by visualizing the search space as an element-wise product
between two matrices.  The (j-i) matrix, and the min(h[i], h[j]) matrix.  If
you know whether h[i] or h[j] is less, then you can know that all volumes

If h[i] < h[j]: V(i, <j) < V(i, j)  # increment i
If h[i] >= h[j]: V(>i, j) < V(i, j) # decrement j

"""
