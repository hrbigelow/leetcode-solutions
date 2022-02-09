class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])
        S = R * C
        rem = k % S

        # record the last k elements
        lastk = []
        for idx in range(S-rem, S):
            lastk.append(grid[idx // C][idx % C])
            
        # update S-k elements in reverse order
        src_idx = S - rem
        for trg_idx in reversed(range(rem, S)):
            r, c = src_idx // C, src_idx % C
            tr, tc = trg_idx // C, trg_idx % C
            grid[tr][tc] = grid[r][c]
            src_idx -= 1

        # copy last k to start
        for idx in range(rem):
            r, c = idx // C, idx % C
            grid[r][c] = lastk[idx]
            
        return grid
    

"""
Approach is to virtually linearize the grid, then perform a rotate forward.
To rotate an array forward k positions, one must do a copy in reverse:


a[i] = a[i-k] for i in reversed(range(k, len(a)))

Then, copy a[:-k] = a[:k]

Uses O(k) memory, does the editing in-place

"""
                
        
        
