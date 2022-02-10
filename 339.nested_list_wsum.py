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
