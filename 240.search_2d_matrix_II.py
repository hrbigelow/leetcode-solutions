class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        def divide(rb, cb, re, ce):
            rm = (rb + re) // 2
            cm = (cb + ce) // 2
            return (
                (rb, cb, rm, cm),
                (rb, cm, rm, ce),
                (rm, cb, re, cm),
                (rm, cm, re, ce)
            )

        def combine(results):
            return any(results)
        
        def search(rb, cb, re, ce, target):
            if rb == re or cb == ce: return False
            if target < matrix[rb][cb] or target > matrix[re-1][ce-1]:
                return False

            if matrix[rb][cb] == target:
                return True
            
            return combine(search(*bound, target) for bound in divide(rb, cb, re, ce))
        
        return search(0, 0, n, m, target)
            
        
"""
This using the divide and conquer template given in the Recurrence II course:

def divide_and_conquer( S ):
    # (1). Divide the problem into a set of subproblems.
    [S1, S2, ... Sn] = divide(S)

    # (2). Solve the subproblem recursively,
    #   obtain the results of subproblems as [R1, R2... Rn].
    rets = [divide_and_conquer(Si) for Si in [S1, S2, ... Sn]]
    [R1, R2,... Rn] = rets

    # (3). combine the results from the subproblems.
    #   and return the combined result.
    return combine([R1, R2,... Rn])

Implementing divide and combine was straightforward.  The recursive 'search' function
was tricky since it wasn't clear at what point to apply the knowledge of the matrix
element ordering for optimizing the search.
"""
