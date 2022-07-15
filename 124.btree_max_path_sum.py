"""

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes in the sequence has an edge connecting them. A node can only appear in
the sequence at most once. Note that the path does not need to pass through the
root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty
path.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')
        def dfs(node):
            if node is None:
                return 0
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            max_downward = max(
                node.val,
                node.val + max_left,
                node.val + max_right
            )
            
            self.max_sum = max(self.max_sum, node.val + max(0, max_left) + max(0, max_right))
            return max_downward
        
        dfs(root)
        return self.max_sum
        
"""
14 min: first draft
16 min: edits
20 min: test ()
29 min: finished (was able to reuse the original recursive definition for return value,
                  while changing the definition of self.max_sum)

Okay, the problem asks for the max path for any path.  In fact this is not much
different than 

Assume that the dfs calculates the max path sum of *any path* which *starts at node*.
Then, what woud its definition be?

If we break it up by the max path *whose highest node is node*, what is its maximum?

No, that definition doesn't work either.

Instead, what we should do is to have the dfs return the max path that *starts at node*,
but, record the max among 


"""
