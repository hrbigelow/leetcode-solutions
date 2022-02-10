class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        inds = [None] + [[float('inf')] * n for _ in range(3)]

        for cind in range(1, 4):
            ind = inds[cind]
            for i, c in enumerate(colors):
                if c == cind:
                    ind[i] = 0
                elif i > 0:
                    ind[i] = ind[i-1] + 1
            
            for i in reversed(range(n-1)):
                ind[i] = min(ind[i], ind[i+1]+1)
            
        ans = [inds[qc][qi] for qi, qc in queries]
        return [-1 if a == float('inf') else a for a in ans]            
        

"""
Does a straight-forward pre-computed cache:

inds[color][i] = distance to nearest 'color' from position i in colors
These are computed in a forward sweep and then backward sweep
"""

