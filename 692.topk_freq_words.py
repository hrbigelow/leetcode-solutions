class LessWordCt:
    def __init__(self, word, ct):
        self.word = word
        self.ct = ct
        
    def __lt__(self, other):
        return self.ct < other.ct or (
            self.ct == other.ct and self.word > other.word)
    
    

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        from collections import Counter

        hist = Counter(words)
        uwords = list(hist.keys())
        heap = [LessWordCt(w, hist[w]) for w in uwords[:k]]
        heapq.heapify(heap)
        
        for w in uwords[k:]:
            lwc = LessWordCt(w, hist[w])
            if heap[0] < lwc:
                heapq.heapreplace(heap, lwc)
        
        heap.sort(reverse=True)
        return [lwc.word for lwc in heap]
        
        
"""
Solved in 26 minutes, with five attempts

Mistakes made:

1. forgot to use the LessWordCt wrapper when building the heap
2. used the raw words list instead of the unique words from the histogram keys
3. erroneously thought that a heap was also sorted when viewed as an array
"""

"""
# WOW!  This is elegant in its use of a tuple, the lambda, and
the count[i] = count.get(i, 0) + 1 construct

However, it doesn't actually make use of the heap itself to reduce
complexity.

import heapq
def topKFrequent(self, words: List[str], k: int) -> List[str]:
    count = dict()
    for i in words:
        count[i] = count.get(i, 0) + 1

    heap_var = [(-val, key) for key,val in count.items()]

    heapq.heapify(heap_var)
    heap_var.sort(key = lambda x: (x[0],x[1]))

    return [x for _,x in heap_var[:k]]
"""



