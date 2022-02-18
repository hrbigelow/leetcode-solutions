# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Analysis of the official solution in terms of the divide-and-conquer template.

In the 'validate' call, (low, high) is the legal (non-inclusive) range that the
whole subtree at root must fall in.  Strangely, though, there is no need to find
the min and max.  All that is needed is to pass these values down for each recursive
call.

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low=-math.inf, high=math.inf):
            # This is the first recursive base case
            if not node:
                return True

            # Unlike my solution, this one passes the legal bounds
            # downwards.  Note that every node is visited on the
            # recursion.  So, 
            if node.val <= low or node.val >= high:
                return False

            # the implicit 'divide' here is calling validate on the
            # left and right sub-trees
            # the 'and' is the 'combine' function
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)
