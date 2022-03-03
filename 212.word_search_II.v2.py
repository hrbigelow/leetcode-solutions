class Trie:
    from collections import defaultdict
    def __init__(self):
        self.children = defaultdict(lambda: Trie())
        self.word_index = None
        
    def get_or_make_child(self, letter):
        return self.children[letter]

    def get_child(self, letter):
        if letter in self.children:
            return self.children[letter]
        return None
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # build the trie
        root = Trie()
        
        for i, w in enumerate(words):
            node = root
            for char in w:
                node = node.get_or_make_child(char)
            node.word_index = i
            
        self.visited = set()
        results = []
        
        nr = len(board)
        nc = len(board[0])
        
        # i, j is current board position to be evaluated
        # node is current trie position to be evaluated
        # up til now, there exists some path in the board matching the
        # path for node.  the root represents the empty path
        def dfs(i, j, node):
            nonlocal nr, nc
            if (i, j) in self.visited:
                return
            
            if not (0 <= i < nr and 0 <= j < nc):
                return

            if board[i][j] not in node.children:
                return

            # we can proceed one step
            parent = node
            node = node.get_child(board[i][j])
            if node is None:
                raise RuntimeError('child should exist but doesn''t')
                
            # extension is valid
            if node.word_index is not None:
                results.append(words[node.word_index])
                node.word_index = None
                
                if len(node.children) == 0:
                    del parent.children[board[i][j]]
            
            self.visited.add((i, j))
            
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(ni, nj, node)
            
            self.visited.remove((i, j))

            
        for i in range(nr):
            for j in range(nc):
                dfs(i, j, root)
                
        return results
            
        
"""
22 min: first draft
33 min: test (failing the singlet board case)
36 min: test (time limit exceeded)
43 min: finished


Why time limit exceeded?  How can we 'clean out' the tree as we are traversing it?

If the node is a leaf and not a word, we can remove it

You could go through each word and search for it, but then the search would not benefit from
the work of finding common prefixes.  

So, to multiplex the search, construct a prefix tree.

Then, for each square on the board, do a search which traverse the board and tree concurrently.

This will be a dfs search, marking each node visited.

At each step in the search, explore board neighbors that have not been visited and whose
values exist in the children of the current node in the tree.

Also, if the current node is marked as the end of a word, add it to the results list.




"""
