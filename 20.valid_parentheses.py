"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

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
