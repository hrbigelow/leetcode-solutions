"""

You are given a 0-indexed string s of even length n. The string consists of
exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

"""

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
