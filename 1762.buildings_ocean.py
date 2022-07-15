"""
There are n buildings in a line. You are given an integer array heights of size
n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the
building can see the ocean without obstructions. Formally, a building has an
ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view,
sorted in increasing order.

"""

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
    
