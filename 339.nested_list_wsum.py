"""
You are given a nested list of integers nestedList. Each element is either an
integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For
example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to
its depth.

Return the sum of each integer in nestedList multiplied by its depth.

"""

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        st = [(ni, 1) for ni in nestedList]
        tot = 0
        while st:
            ni, d = st.pop()
            if ni.isInteger():
                tot += ni.getInteger() * d
            else:
                st.extend([(sni, d+1) for sni in ni.getList()])
        
        return tot
    
"""
Only need isInteger, getInteger and getList
Solved in 7 minutes
Using recursive solution


Solved explicit stack solution in 7 minutes
"""
