class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp, minp = 1, 1
        full_max = -float('inf')
        for el in nums:
            p1 = maxp * el
            p2 = minp * el
            maxp, minp = max(p1, p2, el), min(p1, p2, el)
            full_max = max(full_max, maxp)
        
        return full_max
        
"""
5 min: first draft
10 min: wrong answer (confused the aux variable maxp, which is the max product *ending* at i,
                      with the max product *overall*)
15 min: finished

argument:  if you know both the maxp and minp ending at i-1, then the maxp ending at i should either
be the product of el with the previous minp or maxp, or the element itself.

2,3,-2,4
"""
