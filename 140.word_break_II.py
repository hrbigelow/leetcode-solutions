"""
Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word. Return all
such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

"""

class Node:
    from collections import deque
    
    def __init__(self):
        self.children = {}
        self.ind = None
    
    def set_word(self, ind):
        self.ind = ind
    
    def add_child(self, letter):
        if letter not in self.children:
            self.children[letter] = Node()
        return self.children[letter]
    
    def matches(self, suffix):
        # find all matches for any prefix of s and return a list of tuples
        # [(ind, depth), ...]
        matches = []
        dq = deque()
        dq.append((self, 0))
        
        while dq:
            node, i = dq.popleft()
            if node.ind is not None:
                matches.append(node.ind)

            if i >= len(suffix):
                continue

            for letter, child in node.children.items():
                if letter == suffix[i]:
                    dq.append((child, i+1))
        
        return matches
            
            

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # construct tree
        tree = Node()
        for ind, w in enumerate(wordDict):
            node = tree
            for letter in w:
                node = node.add_child(letter)
            node.set_word(ind)
    
        sentences = []
        n = len(s)
        def dfs(path, pos):  
            # continue augmenting path starting from s[pos:]
            # print(path, pos)
            if pos == n:
                sentences.append(' '.join(wordDict[ind] for ind in path))
                return
            
            if pos > n:
                return
            
            # query the tree with s[pos:] looking for inds
            for ind in tree.matches(s[pos:]):
                dfs(path + [ind], pos + len(wordDict[ind]))
        
        dfs([], 0)
        
        return sentences
                               
                
        
"""
Solved in 1 hour 7 minutes

I was disciplined and spent some good analysis mentally debugging.  However, I resorted to one print statement.
After that, it was easy to narrow down the bug.

Overview:

1. Construct a prefix tree of the dictionary, with nodes holding an index of the word they represent, if
it is present in the dictionary.

The tree supports a sequence search, which returns a list of indices found

2. Do a DFS on the query string, using indseqs as an accumulator. 

3. Finally, 

There is a bug.  I have a hunch it is in the matches routine


"""
