class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def dfs(counts, level, remain):
            if level == n:
                if remain == 0:
                    res.append([c for (ct, can) in zip(counts, candidates) for c in [can] * ct])
                return
            can = candidates[level]
            for ct in range(remain // can + 1):
                dfs(counts + [ct], level + 1, remain - ct * can)
        
        dfs([], 0, target)
        return res
    
"""
This is a truncated depth-first-search recursion.  Each path represents a distinct set of coefficients
for the candidates, passed as 'counts'.  The result array res is the corresponding set of combinations.

Importantly, the counts structure is a convenient, compact intermediate representation, since it doesn't grow
to a size larger than n, while the combinations themselves, containing repeats, may be very long.

"""
