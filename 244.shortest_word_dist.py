"""
Design a data structure that will be initialized with a string array, and then
it should answer queries of the shortest distance between two different strings
from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array
wordsDict.

int shortest(String word1, String word2) returns the shortest distance between
word1 and word2 in the array wordsDict.

"""

from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locs = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.locs[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        md = float('inf')
        l, r = 0, 0
        wl = self.locs[word1]
        wr = self.locs[word2]
        
        while l != len(wl) and r != len(wr):
            md = min(md, abs(wl[l] - wr[r]))
            if wl[l] < wr[r]:
                l += 1
            else:
                r += 1
        return md
    
                     
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)


"""
I gave up after one hour.  But, it turned out that the best
idea I had was actually the same as the published solution.  I rejected
it because it was still O(N) for each query.

The idea is to store a sorted list of locations for each word in the index.
Then, for each query, do a tandem forward pass through the two word location lists,
accumulating the minimum distance found, and return it.

"""
