"""
Idea is to traverse the virtual graph
Nodes are (val, count)
Edges connect any node from lower to higher val.

This is a classic backtracking problem, with 'budget' keeping track of the remaining
quantity that can be summed.

"""

from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cts = sorted(list(Counter(candidates).items()))
        n = len(cts)
        combos = []
        def extend(idx, path, budget):
            # path: [(val, quantity), (val, quantity), ... ]
            # idx: explore cts[idx:]
            # budget:  amount of `target` left to populate
            if budget == 0:
                combo = [ [val] * ct for val, ct in path ]
                combo = [ v for el in combo for v in el ]
                combos.append(combo)
                return
            for t in range(idx, n):
                val, ct = cts[t]
                if val > budget:
                    return
                for q in range(1, ct+1):
                    if val * q <= budget:
                        extend(t+1, path + [(val, q)], budget - val * q)
        
        extend(0, [], target)
        return combos

