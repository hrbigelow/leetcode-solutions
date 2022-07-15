"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        st = []
        n = len(height)
        for i in range(n):
            pre = None
            while st and height[st[-1]] <= height[i]:
                pre_height = 0 if pre is None else height[pre]
                step = height[st[-1]] - pre_height
                vol += step * (i - st[-1] - 1)
                pre = st.pop()
            if st and pre:
                vol += (min(height[st[-1]], height[i]) - height[pre]) * (i - st[-1] - 1)
                
            st.append(i)
        
        return vol
            
"""
min 8: first draft
min 18: test (corrected mistake of neglecting the pre height)
min 42: finished (corrected bug of line 14 (i - pre vs i - st[-1] - 1))

While processing the less-equal elements of the stack,
the first one popped has no pre, so sets no height.
After that

"""
