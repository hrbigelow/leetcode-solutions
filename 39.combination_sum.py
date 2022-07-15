"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

It is guaranteed that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.
"""

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
