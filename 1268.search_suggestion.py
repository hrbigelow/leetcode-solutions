"""

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after
each character of searchWord is typed. Suggested products should have common
prefix with searchWord. If there are more than three products with a common
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of
searchWord is typed.

"""

class CharNode:
    def __init__(self):
        self.children = {}
        self.inds = []
    
    def add_word(self, ind):
        if len(self.inds) != 3:
            self.inds.append(ind)
    
    def get_child(self, letter):
        if letter not in self.children:
            self.children[letter] = CharNode()
        return self.children[letter]
            

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        root = CharNode()
        for i, p in enumerate(products):
            node = root
            for letter in p:
                node = node.get_child(letter)
                node.add_word(i)
        
        sugg = []
        node = root
        for sw in searchWord:
            node = node.get_child(sw)
            sugg.append([products[i] for i in node.inds])
        
        return sugg

    
"""
Solved in 24 minutes

I knew it was a prefix tree type of approach.  I considered both BFS and DFS approaches to building
the initial list.  BFS would be to process the first position of each product word, then the second, etc.
It was inconvenient since it would require storing the position of each leading node on its downward pathway.
DFS was the way to go - process an entire word at a time.

I realized that each node should store the indices of the first three words with the prefix which the node represents.
At first this seemed very tricky, like it would require inspecting the set of indices.  But, then I realized that if you
simply sort the product words, and then store the first three that are added to the node after it is created, this will
naturally be the correct three.


"""
