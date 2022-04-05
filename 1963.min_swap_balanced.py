class Solution:
    def minSwaps(self, s: str) -> int:
        depth = 0
        nswap = 0
        for ch in s:
            if ch == ']':
                if depth == 0:
                    nswap += 1
                    depth += 1
                else:
                    depth -= 1
            else:
                depth += 1
        return nswap
        
"""
Finished in 12 minutes.  I solved this just by reasoninig that at each
step, you either are forced to swap, or not.  And, if not forced to swap,
then by some wishy-washy reasoning, you should not swap, because that will
minimize the number of swaps.

Since it is known that there are an equal number of open and closed brackets,
we know that if we make just the swaps that are necessary and no more, we're guaranteed
to end up with a balanced string.

"""
