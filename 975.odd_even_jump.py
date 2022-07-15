"""
You are given an integer array arr. From some starting index, you can make a
series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called
odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called
even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j
such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there
are multiple such indices j, you can only jump to the smallest such index j.

During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j
such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there
are multiple such indices j, you can only jump to the smallest such index j.

It may be the case that for some index i, there are no legal jumps.

A starting index is good if, starting from that index, you can reach the end of
the array (index arr.length - 1) by jumping some number of times (possibly 0 or
        more than once).

Return the number of good starting indices.

"""

class Solution:
    from functools import lru_cache
    
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        # insert (or replace) i into inds according to the mapping provided by arr
        # return the previous lower bound and upper bound together
        inds = []
        def insert(i):
            nonlocal inds
            k = len(inds)
            lo, hi = 0, k
            v = arr[i]
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[inds[mid]] < v:
                    lo = mid + 1
                else:
                    hi = mid
            
            # lo is the index of least upper bound (and the insertion point)
            
            ub = None if lo == k else inds[lo]
                        
            if lo != k and arr[inds[lo]] == v:
                lb = inds[lo]
                inds[lo] = i # replace equal element
            else:
                lb = None if lo == 0 else inds[lo-1]
                inds.insert(lo, i)
            return lb, ub
        

        lb = [None] * n
        ub = [None] * n
        for i in reversed(range(n)):
            lb[i], ub[i] = insert(i)
            # print(inds)

        # print('lower bound:', lb)
        # print('upper bound:', ub)
        
        
        @lru_cache
        def rec(i, odd_start):
            # print(i, odd_start)
            # tell whether jumping from position i and whether it is an odd numbered (ones-based)
            # starting jump is a good one
            if i is None:
                return False
            
            if i == n-1:
                return True
        
            j = ub[i] if odd_start else lb[i]
            return rec(j, not odd_start)
            
        return sum(int(rec(i, True)) for i in reversed(range(n)))
                
            
        
"""
This took about 2 hours.  The first pass solution I had in 30 minutes, using a linear forward scan
for both the lower and upper bounds.  The second pass I used an erroneously conceived stack-based
idea.  The third solution you see here.  It is an O(n log n) mechanism, building a sorted list with
successive 

For any given i and parity, j is uniquely determined or doesn't exist

We can cache the (i, parity) goodness as a bool.
"""
