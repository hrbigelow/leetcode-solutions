"""
There are n workers. You are given two integer arrays quality and wage where
quality[i] is the quality of the ith worker and wage[i] is the minimum wage
expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k
workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality
compared to other workers in the paid group.

Every worker in the paid group must be paid at least their minimum wage
expectation.

Given the integer k, return the least amount of money needed to form a paid
group satisfying the above conditions. Answers within 10-5 of the actual answer
will be accepted.

"""

class Solution:
    import heapq
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        inds = sorted(range(n), key=lambda i: wage[i] / quality[i])
        
        qualities = [quality[inds[i]] for i in range(n)]
        priciness = [wage[inds[i]] / quality[inds[i]] for i in range(n)]

        heap = [-q for q in qualities[:k]]
        heapq.heapify(heap)
        
        total_quality = -sum(heap)
        min_cost = total_quality * priciness[k-1]
        for i in range(k, n):
            max_qual = -heap[0]
            if qualities[i] < max_qual:
                total_quality -= max_qual
                total_quality += qualities[i]
                heapq.heapreplace(heap, -qualities[i])
                min_cost = min(min_cost, total_quality * priciness[i])
        
        return min_cost
    
"""
1. compute priceyness (wage / quality)


The total pay will be max(p[i]) * sum(quality[i]) over the i

Therefore, one could scan through each i from range(k, n), in order
of increasing priceyness.  Each new priceyness at i, if quality[i] < heap[0], 
replace it.


"""
