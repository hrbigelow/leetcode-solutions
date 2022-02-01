

# 168 ms
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0
        num_islands = 0
        nrows, ncols = len(grid), len(grid[0])
        
        def helper(r, c, grid):
            """
            zero-out this island identified by r, c
            """
            from collections import deque
            dq = deque()
            dq.append((r, c))
            grid[r][c] = "0"
            dirs = { (0,1), (0,-1), (-1,0), (1,0) }
            
            while dq:
                r, c = dq.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(nrows) and nc in range(ncols) and grid[nr][nc] == "1":
                        dq.append((nr, nc))
                        grid[nr][nc] = "0"
                        #print(nr, nc, grid[nr][nc])

                        # print(dq)
            return                
            
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    num_islands += 1
                    helper(r, c, grid)
                    # print(grid)
        return num_islands
    
 
 


# 116 ms
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        max_x = len(grid)
        max_y = len(grid[0])
        
        num_islands = 0
        
        def spread(x,y):
            grid[x][y] = '2'
            if x-1 >= 0 and grid[x-1][y] == '1':
                spread(x-1,y)
            if x+1 < max_x and grid[x+1][y] == '1':
                spread(x+1,y)
            if y-1 >= 0 and grid[x][y-1] == '1':
                spread(x,y-1)
            if y+1 < max_y and grid[x][y+1] == '1':
                spread(x,y+1)
        
        for x in range(0,max_x):
            for y in range(0,max_y):
                if grid[x][y] == '1':
                    num_islands +=1
                    spread(x,y)
                    
        return num_islands

