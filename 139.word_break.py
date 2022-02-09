class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        st = [0]
        dead = set()
        while st:
            pos = st.pop()
            dead.add(pos)
            for w in wordDict:
                end = pos+len(w)
                if s[pos:end] != w:
                    continue
                if end == n:
                    return True
                if end not in dead:
                    st.append(end)
        return False

"""
This is an explicit-stack depth-first search solution using caching.

"""
