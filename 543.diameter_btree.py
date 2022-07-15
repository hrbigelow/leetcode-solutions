"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # returns length of longest descending path
        # calculates length of longest path with node as highest point
        max_width = 0
        
        def dfs(node):
            nonlocal max_width
            if node is None:
                return 0
            num_nodes_left = dfs(node.left)
            num_nodes_right = dfs(node.right)
            max_width = max(max_width, num_nodes_left + num_nodes_right)
            # print(node.val, max_width)
            return max(num_nodes_left, num_nodes_right) + 1

        _ = dfs(root)
        return max_width
    
        
"""
7 min: first draft
10 min: test (wrong answer)
18 min: finished (I misunderstood the meaning of 'length' to mean "number of nodes in the path")

This was pretty straightforward, except that it is easier to count 'number of nodes' rather than 'length'
since number of nodes is easily extendible from the base case of 'zero nodes'.  Length is not as easy.

"""
