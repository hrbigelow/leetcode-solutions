class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        
        # record all patterns starting with prefix, which
        # can be completed with the number of open parens
        # available, and current stack depth
        def backtrack(prefix, stack_depth, num_open_avail):
            if num_open_avail == 0 and stack_depth == 0:
                self.results.append(prefix)
            
            if stack_depth != 0:
                backtrack(prefix + ')', stack_depth-1, num_open_avail)
                
            if num_open_avail != 0:
                backtrack(prefix + '(', stack_depth+1, num_open_avail-1)
            
        backtrack('', 0, n)
        return self.results
    
                
        
        
"""
8 min: first draft
20 min: finished

Worked on first submission.  I had to think carefully about whether to record
num_close_avail or num_open_avail.  Also, briefly, I wondered whether there was
potential for infinite recursion by simply opening parens indefinitely.
"""
