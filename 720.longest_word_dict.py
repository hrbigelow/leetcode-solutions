class Solution:
    from collections import deque
    def longestWord(self, words: List[str]) -> str:
        sorted_words = sorted(words)
        # print(sorted_words)
        path = ['']
        max_word = ''
        
        # print(len(words))
        for w in sorted_words:
            while len(path[-1]) >= len(w) and path[-1] != w[:-1]:
                path.pop()
            
            if path[-1] == w[:-1]:
                path.append(w)

            if len(path) > len(max_word) + 1:
                max_word = path[-1]
            
            # print(path)

        return max_word
        
        
"""
Took 1.5 hours
This came up on a Facebook Onsite practice test.  I spent a long time
trying to ponder the solution using just a single 'prefix' and 'extension',
but ultimately forgot to consider cases such as:

a ab abc ad

where ad must be considered an extension of a, even though abc was a successful extension of ab.

This example immediately suggested a stack.
"""
