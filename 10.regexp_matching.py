class Solution:
    import re
    def isMatch(self, s: str, p: str) -> bool:
        pats = re.findall('[\.a-z](?!\*)|[\.a-z]\*', p)
        pre = [False] * (len(pats) + 1)
        
        for ch in '$' + s:
            cur = [ch == '$'] + [True] * len(pats)
            for j, pat in enumerate(pats, start=1):
                if len(pat) == 2:
                    # A Star pattern can extend the previous, or not match at all
                    valid = (pre[j] and pat[0] in ('.', ch)) or cur[j-1]
                else:
                    # A dot or char pattern must match exactly one
                    valid = pre[j-1] and (pat in ('.', ch))
                    
                cur[j] = valid
            pre = cur
        
        return cur[-1]
    
"""
Took 4 hours and about 20 attempts.  I quickly settled on a 2D DP solution.  It
took awhile to derive the rules.  There were three rules which looked up, to
the left, and diagonally up and left.  Besides this, I misread the question and
didn't recognize that '.*' could be one of the pattern tokens.

The full DP matrix has ns+1 rows, and np+1 columns.  The main loop iterates
using pre, cur as a pair of rows, starting with cur being the first row of the
matrix.  The difficulty is in setting cur[0].  The first iteration, it is true,
but is false on all subsequent iterations because:  the first iteration
represents the empty string, which matches the empty pattern.  A non-empty
string never matches an empty pattern.

Strategies:

1. Always first visualize the full structure that you are creating.  In this
case, it is the full DP matrix.  Then, be explicit about the strategy for
virtually computing it.  In this case, it is to use a pre and cur pair of rows,
where cur starts at the first row.

Finally, the DP production rules could be expressed either as forwards pointing
or backwards pointing.  In the backward-pointing style, a given result is
computed from up to three predecessors.  In the forward-pointing style, one
predecessor is used to partially compute up to three results, and the final
result needs to be a combination of these partial computations.
"""
