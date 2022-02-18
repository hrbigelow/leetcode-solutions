"""
Took about 25 minutes to implement both recursive and iterative approaches.  I first
implemented a DFS recursive approach, then just used a typical conversion tactic to
convert it to a deque-based BFS.

We are doing a DFS on a virtual tree.  The path can go left (adding an open paren) if there are more
open parens remaining.  It can go right if depth > 0.  When both paths are exhausted, it is a leaf
and we record the result

One approach could be to push to a deque the tuples (expr, depth, num_open_remain)
and to keep them until the end

"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from collections import deque
        d = deque([('', 0, n)])
        results = []
        while d:
            expr, depth, n_open_remain = d.popleft()
            
            if depth > 0:
                d.append((expr + ')', depth-1, n_open_remain))
                
            if n_open_remain > 0:
                d.append((expr + '(', depth+1, n_open_remain-1))
                
            if depth == 0 and n_open_remain == 0:
                results.append(expr)
        
        return results
    
        
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        
        # starting at indentation depth with expr and k open parens left,
        # produce all valid continuations of expr
        def gen_rec(depth, expr, n_open_remain):
            if n_open_remain == 0 and depth == 0:
                results.append(expr)
                return
            
            if depth > 0:
                gen_rec(depth-1, expr + ')', n_open_remain)

            if n_open_remain > 0:
                gen_rec(depth+1, expr + '(', n_open_remain-1)
            
        gen_rec(0, '', n)
        return results
"""
