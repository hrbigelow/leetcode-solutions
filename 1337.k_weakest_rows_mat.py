class Solution:
    import heapq
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        h = [(- sum(mat[i]), -i) for i in range(k)]
        heapq.heapify(h)
        for i in range(k, n):
            neg_strength = -sum(mat[i])
            if (neg_strength, -i) > h[0]:
                heapq.heapreplace(h, (neg_strength, -i))
        
        results = []
        while h:
            results.append(-heapq.heappop(h)[1])
        return reversed(results)
    
"""
we want the k rows with minimal sum(mat[i]).

So, we want to use a max heap, and keep replacing the maximum with
a lesser row if it occurs.

then, if same sum, replace with lesser index

"""
