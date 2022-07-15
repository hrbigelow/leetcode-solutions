"""

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

"""

class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        dq = deque()
        num_islands = 0
        
        for start_row in range(nr):
            for start_col in range(nc):
                if grid[start_row][start_col] == '0':
                    continue
                dq.append((start_row, start_col))
                is_island = False
                while dq:
                    r, c = dq.popleft()
                    # if not (0 <= r < nr and 0 <= c < nc):
                    #     continue
                    if grid[r][c] == '0':
                        continue
                    is_island = True
                    grid[r][c] = '0'
                    # dq.extend([(r+1, c), (r-1, c), (r, c+1), (r, c-1)])
                    dq.extend([(new_r, new_c) for new_r, new_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                              if 0 <= new_r < nr and 0 <= new_c < nc ])
                               # and grid[new_r][new_c] == '1'])
                    # print(dq)
                
                num_islands += int(is_island)
        
        return num_islands
    
        
"""
6 min: first draft
9 min: finished (weird - I did 0 < r <= nc instead of 0 <= r < nc)

I played around with this.  It seems like if you only check that certain neighbors are
island when *scheduling* them, you do duplicate work.  If instead, you check when you actually
visit, then it is O(n).  So, this is a critical difference

For each square do a BFS, marking each as visited.
Alternatively, change the grid to zeros while visiting, which is allowed
Remember the grid holds strings, not int
Do the 
"""
