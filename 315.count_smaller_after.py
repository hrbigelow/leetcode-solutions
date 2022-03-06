class Solution:
    def insert_point(self, a, val):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
    
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ordered = []
        results = [None] * n
        for i in reversed(range(n)):
            j = self.insert_point(ordered, nums[i])
            results[i] = j
            ordered.insert(j, nums[i])
        
        return results
    
"""
6 min: first draft
9 min: test (wrong answer)
27 min: first draft of new idea
29 min: finished (no issues)

"""
