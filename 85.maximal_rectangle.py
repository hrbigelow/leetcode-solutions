class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Taken from a user submission
        m, n  = len(matrix), len(matrix[0])
        c = [0] * (n+1)
        ans = 0
        for i in range(m):
            q = []
            for j in range(n+1):
                if j < n:
                    if matrix[i][j] == '1':
                        c[j] += 1
                    else:
                        c[j] = 0
                k = j
                while q and q[-1][1] > c[j]:
                    k, h = q.pop()
                    ans = max(ans, h * (j - k))
                if not q or c[j] > q[-1][1]:
                    q.append((k, c[j]))
            # for k, h in q:
            #     ans = max(ans, h * (n - k))
        return ans
    
    
        
"""
Analysis:

c[j] is the vertical runlength at column j,
up to the current row in the matrix.  Think of it as
a skyline.  The task is to find the largest rectangle
contained under that skyline.

q is the classic stack which records only increasing
runs.  When a decrease is encountered, things are popped
until the stack can be pushed to be increased.

This technique is a classic one which allows finding, for
each element, the greatest preceding element less than it.

For the skyline, this is equivalent to extending a given
rectangle (whose element is the current height) as far back
as it can go.

To see why this involves "nested structure", imagine instead an
arbitrary function and searching for the maximal rectangle under it.
Each candidate rectangle would be defined by its top edge, which must
touch the graph at both end points.  You would note that drawing
all such edges which touch the graph creates a nested structure.

This nested structure is harder to see for a piecewise-constant graph,
but it does exist.

"""
