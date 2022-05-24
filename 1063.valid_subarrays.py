class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        st = []
        tot = 0
        for v in nums:
            while st and st[-1] > v:
                st.pop()
            tot += len(st) + 1
            st.append(v)
        
        return tot
        
        
"""
Solved in 9 minutes.  I got lucky
"""
