"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds
is divisible by 60. Formally, we want the number of indices i, j such that i <
j with (time[i] + time[j]) % 60 == 0.  from collections import defaultdict

"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        trg = defaultdict(lambda: 0)
        ct = 0
        for sec in time:
            m = sec % 60
            if m in trg:
                ct += trg[m]
            trg[0 if m == 0 else 60-m] += 1
        
        return ct

"""
The tricky thing is, upon seeing a value sec, we want the following 
relationship to hold:

sec%60    target
0         0
1         59
...
59        1

it cannot just be 60 - (sec % 60)
"""
