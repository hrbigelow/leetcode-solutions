"""

A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.


"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word2masked = {}
        masked2word = {}
        
        for word in [beginWord] + wordList:
            ww = word + '$' + word
            wn = len(word)
            masks = [ww[i:i+wn] for i in range(1, wn+1)]
            word2masked[word] = masks
            for m in masks:
                if m not in masked2word:
                    masked2word[m] = []
                masked2word[m].append(word)
            
            
        def nbors(word):
            return [w for m in word2masked[word] for w in masked2word[m] if w != word]
        
        # BFS
        from collections import deque
        
        visited = set()
        dq = deque()
        dq.append((beginWord, 1))
        while dq:
            word, dist = dq.popleft()
            if word in visited:
                continue
                
            visited.add(word)
                
            if word == endWord:
                return dist
            
            dq.extend((w, dist+1) for w in nbors(word))
            
        return 0
        
        
        
"""
18 min: first draft
20 min: test (deque init problem)
21 min: test (key error)
25 min: test (edge case of length-1 words)
38 min: finished (had stupid mistake to add beginWord to visited)

The wordList defines a set of graph nodes
The diff_by_one() function defines edges

The problem just asks for length of shortest path, or 0 if none exists

I forgot Dijkstra's shortest path algo.  But, BFS also finds it.

The problem is the construction of edges is O(N^2), or is it.

Could we use a mismatch tree, is there such a thing?


l = len(beginWord)

How to find a word's neighbors?

for each i:
    word -> masked_word[i]
    masked_word[i] -> neighbors
    
Then just use BFS




"""
