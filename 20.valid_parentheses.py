class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(':
                st.append(')')
            elif ch == '[':
                st.append(']')
            elif ch == '{':
                st.append('}')
            
            elif not st or ch != st[-1]:
                return False
            
            else:
                st.pop()
        
        return not st
        
"""
6 min first draft
8 min finished

No issues, worked on first try

"""
