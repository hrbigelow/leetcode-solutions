"""
Given the root of a binary tree, determine if it is a valid binary search tree
(BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key.  The right subtree of a node contains only nodes with keys greater than the
node's key.  Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
To validate, we need to validate the left and the right sub-trees, and also
find the max value of the left and min value of the right, and test if they are
well ordered with root.val.

So, we will return a tuple min, max, valid for the recursive call


This took several tries.  The combine function was tricky.
I mistakenly was returning lmin, rmax as the last two arguments unconditionally,
rather than the below expression.

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def divide(node):
            return node.left, node.right
    
        def validate(node):
            if node is None:
                return True, None, None
            
            return combine(node, *(validate(sub) for sub in divide(node)))
            
        
        def combine(node, left_sub, right_sub):
            lvalid, lmin, lmax = left_sub
            rvalid, rmin, rmax = right_sub
            return (
                lvalid and rvalid and
                (lmax is None or lmax < node.val) and
                (rmin is None or rmin > node.val),
            node.val if lmin is None else lmin,
            node.val if rmax is None else rmax
            )
                
        return validate(root)[0]
        
