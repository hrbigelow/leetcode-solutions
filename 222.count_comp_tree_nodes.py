# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def lmdepth(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth
        
        num_nodes = 0
        ld = rd = None
        node = root
        
        while node is not None:
            num_nodes += 1  # count the current node
            if ld is None:
                ld = lmdepth(node.left)
            if rd is None:
                rd = lmdepth(node.right)
                
            if ld == rd:
                # left sub-tree is complete, move to the right
                num_nodes += 2**ld - 1
                ld = rd-1
                rd = None
                node = node.right
                
            else:
                # right sub-tree is complete, move to the left
                num_nodes += 2**rd - 1
                ld -=1
                rd = None
                node = node.left
                
        return num_nodes
        
"""
40 min: first draft
50 min: finished

Took awhile to reason through it.  I got the complexity analysis correct, O(log^2 N)

I forgot to count the current node each time.  Otherwise, the logic was sound.

"""
