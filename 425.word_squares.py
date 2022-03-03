class Solution:
    import bisect
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        W = len(words)
        words = sorted(words)
        results = []
        
        def backtrack(square):
            next_i = len(square)
            if next_i == n:
                results.append(square.copy())
                return
                
            pfx = ''.join(w[next_i] for w in square)
            wi = bisect.bisect_left(words, pfx)
            
            while wi != W and words[wi].startswith(pfx):
                # print(wi, words[wi])
                square.append(words[wi])
                backtrack(square)
                square.pop()
                wi += 1
        
        backtrack([])
        
        return results
        
        
"""
19 min: first draft
32 min: finished

I mistakenly used n instead of W as the number of words at the top-level to cycle through.

Otherwise, the backtracking approach and the overall design were solid.
"""
