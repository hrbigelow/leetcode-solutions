"""
Android devices have a special lock screen with a 3 x 3 grid of dots. Users can
set an "unlock pattern" by connecting the dots in a specific sequence, forming
a series of joined line segments where each segment's endpoints are two
consecutive dots in the sequence. A sequence of k dots is a valid unlock
pattern if both of the following are true:

All the dots in the sequence are distinct.
If the line segment connecting two consecutive dots in the sequence passes
through the center of any other dot, the other dot must have previously
appeared in the sequence. No jumps through the center non-selected dots are
allowed.

For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand
is valid because the line from dot 2 to dot 9 does not pass through the center
of either dot 5 or 6.

However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid
because the line from dot 1 to dot 3 passes through the center of dot 2.
"""

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        # generate the 'fly-over' dictionary
        fly_over = {
            (1,3): 2,
            (3,1): 2,
            (4,6): 5,
            (6,4): 5,
            (7,9): 8,
            (9,7): 8,
            (1,7): 4,
            (7,1): 4,
            (2,8): 5,
            (8,2): 5,
            (3,9): 6,
            (9,3): 6,
            (1,9): 5,
            (9,1): 5,
            (3,7): 5,
            (7,3): 5
        }
       
        self.num_pats = 0
        
        self.visited = set()
        
        # find all valid patterns which start with the valid pattern
        # of length 'length' which ends at pos (including pos)
        # self.visited does not include pos, however, it is added before
        # recursion
        def backtrack(pos, length):
            
            if length >= m:
                self.num_pats += 1
            if length == n:
                return
            
            self.visited.add(pos)
            for next_pos in range(1, 10):
                if next_pos in self.visited:
                    continue
                if fly_over.get((pos, next_pos), pos) not in self.visited:
                    continue
                backtrack(next_pos, length+1)
            self.visited.remove(pos)
        
        for pos in range(1, 10):
            backtrack(pos, 1)
        
        return self.num_pats
    
                    
"""
14 min: first draft
25 min: test (wrong answer)
28 min: finished

I inspected the lines and the logic of the 'if fly_over ...' line was wrong.
If the entry is NOT in fly_over, it means that there shouldn't be a filter.

"""
