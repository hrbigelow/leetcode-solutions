class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letter_map = [
            None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
        ]
        
        self.results = []
        self.digits = [int(d) for d in digits]
        
        # generate all combos starting with prefix, and
        # continued with digits[i:]
        def combos(prefix, i):
            if i == len(self.digits):
                if i != 0:
                    self.results.append(prefix)
            else:
                for letter in self.letter_map[self.digits[i]]:
                    combos(prefix + letter, i+1)
        
        combos('', 0)
        return self.results
    
"""
5 min: first draft
7 min: test (failed the empty edge case)

This is simple recursion.  

combos(prefix, remain):


"""
