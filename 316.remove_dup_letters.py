"""
Given a string s, remove duplicate letters so that every letter appears once
and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        end_pos = {c: i for i, c in enumerate(s)}
        st = []
        for i, c in enumerate(s):
            if c in st:
                continue
            while st and c < st[-1] and i < end_pos[st[-1]]:
                st.pop()
            st.append(c)
        
        return ''.join(st)
        
"""
The idea is that after each character in the source string is processed, the stack contains the smallest deduplicated
string in the source string up until that point.

Lines 6-7 prevent considering a duplicate character.
Lines 8-9 say that, if we encounter some character c which is less than that
at the end of the stack, and the character at the end of the stack happens to
be available somewhere later in the string (i.e. i < end_pos[st[-1]]) then we can
decrease the ordering.

"""
