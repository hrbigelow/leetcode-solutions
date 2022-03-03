class Solution:
    from collections import deque, defaultdict
    
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        by_x = defaultdict(lambda: [])
        by_y = defaultdict(lambda: [])
        
        for i, (x, y) in enumerate(stones):
            by_x[x].append(i)
            by_y[y].append(i)

            
        component = [None] * n
        comp_num = 0
        dq = deque()
        for i in range(n):
            if component[i] is not None:
                continue
            
            component[i] = comp_num
            dq.append(i)

            while dq:
                i = dq.popleft()
                for j in by_x[stones[i][0]]:
                    if component[j] is None:
                        component[j] = comp_num
                        dq.append(j)
                
                for j in by_y[stones[i][1]]:
                    if component[j] is None:
                        component[j] = comp_num
                        dq.append(j)
                        
            comp_num += 1
            dq.clear()
            
        return n - comp_num
        
"""
10 min: first draft
17 min: finished

seemed pretty straightforward after reasoning through it.

Basically, you just want to count the number of connected components of the graph
The graph is such that stones are nodes and edges connect any two stones that share
a row or column.

Then, if k is the number of connected components, n the total number of stones, then you can remove
n-k stones, leaving one stone for each component.

Question is, then, how to find the number of connected components in a graph?


Keep an array labeling each stone with its component.

"""
