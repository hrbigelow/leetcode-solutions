class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = []
        n = len(heights)
        for i in range(n):
            while st and heights[st[-1]] <= heights[i]:
                st.pop()
            st.append(i)
        
        return st

"""
Solved in 3 minutes.  First part was to realize how to solve it inductively and
then maintain this solution upon the addition of a building to the rigt.
"""    
    
