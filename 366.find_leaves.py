"""
Given the root of a binary tree, collect a tree's nodes as if you were doing
this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
"""

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def find_rec(node):
            from itertools import zip_longest
            if node is None: return []
            l = find_rec(node.left)
            r = find_rec(node.right)
            m = [li + ri for li, ri in zip_longest(l, r, fillvalue=[])]
            m.append([node.val])
            return m
            
        return find_rec(root)
        
        
"""
Solved in 5 minutes

The recursive solution is easiest to think about.  Assume you have a solution for a base case
and know how to combine the solution for the left and right subtrees to a solution for the main tree.

"""
