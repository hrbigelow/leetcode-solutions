import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for e in nums[k:]:
            if e > h[0]:
                heapq.heapreplace(h, e)
        
        return h[0]

"""
Straightforward binary heap solution which is N log(K).  One gotcha is to
make sure you're using a min heap rather than max heap, since the min heap
allows increasing the min.  The min-heap provides a lower bound on its contents,
which can be increased.
"""
