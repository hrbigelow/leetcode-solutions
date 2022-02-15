class Node:
    def __init__(self):
        self.count = 0
        self.word_ind = None
        self.children = {}
        
    def add_child(self, letter):
        self.count += 1
        if letter not in self.children:
            self.children[letter] = Node()
        return self.children[letter]
    
    def set_word(self, ind):
        self.word_ind = ind
        self.count += 1

    def find_next(self, letter):
        if letter in self.children:
            return self.children[letter]
        return None
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R = len(board)
        C = len(board[0])
        
        visited = [[False] * C for _ in range(R)]
        
        # build prefix tree
        tree = Node()
        for i, w in enumerate(words):
            node = tree
            for c in w:
                node = node.add_child(c)
            node.set_word(i)
        
        # node is the current position in the tree
        # r, c is current grid position
        found = []
        
        def dfs(node, r, c):
            if node is None or node.count == 0: return 0
            
            if node.word_ind is not None:
                found.append(words[node.word_ind])
                node.word_ind = None
                node.count -= 1

            if not 0 <= r < R or not 0 <= c < C or visited[r][c]:
                return 0

            visited[r][c] = True
            nfound = 0
            
            child = node.find_next(board[r][c])
            nfound += dfs(child, r-1, c)
            nfound += dfs(child, r+1, c)
            nfound += dfs(child, r, c-1)
            nfound += dfs(child, r, c+1)

            visited[r][c] = False

            node.count -= nfound
            return nfound
        
        
        for r in range(R):
            for c in range(C):
                nfound = dfs(tree, r, c)
                tree.count -= nfound
                
                
        return found
    
                
        
"""

"""
