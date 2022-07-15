"""
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
"""

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1

        return [num for num,ct in sorted(dd.items(), key=lambda i: i[1])[-k:]]
        
        
"""
First thought:
in one pass, compile a counter, then iterate through the top k keys

Finished in 9 minutes
Confused key and value (incorrectly sorted by key rather than value)
Also, confused the expression a[:-k] and a[-k:] when I wanted the 'last k items in a'
"""


"""
This O(N) solution provided in the comments.  It seems to use the
same amortization trick as allows a Hash to do O(1) retrieval.
That is, since it is known that the values in the array are bounded,
one can sort them using the radix sort technique.

"""
# def topKFrequent(self, nums, k):
#     bucket = [[] for _ in range(len(nums) + 1)]
#     Count = Counter(nums).items()
#     for num, freq in Count: bucket[freq].append(num)
#     flat_list = [item for sublist in bucket for item in sublist]
#     return flat_list[::-1][:k]


