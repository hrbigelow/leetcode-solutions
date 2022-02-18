class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        # sublist of distinct numbers has been accumulated,
        # with the previous element pre_elem.  explore all
        # valid completions of the list with k more elements
        def backtrack(sublist, k, n):
            if k == 0:
                results.append(sublist.copy())
                return
            
            pre_elem = 0 if not sublist else sublist[-1]
            for el in range(pre_elem + 1, n):
                sublist.append(el)
                backtrack(sublist, k-1, n)
                sublist.pop()
                
        backtrack([], k, n+1)
        return results
    
"""
Completed in about 10 minutes.  Nothing was tricky here, since the results were simply
appended to a global results array, and the backtrack function didn't need to return anything.

The validity test is implicit in the for loop, which starts from pre_elem + 1.  This prevents adding
duplicate elements to each sublist.
"""
