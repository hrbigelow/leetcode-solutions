# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def feq(node1, node2):
            # base cases
            if node1 is None and node2 is None:
                return True
            
            elif node1 is None or node2 is None:
                return False
            
            else:
                return (
                node1.val == node2.val and (
                    (feq(node1.left, node2.left) and feq(node1.right, node2.right)) or
                    (feq(node1.left, node2.right) and feq(node1.right, node2.left))
                    )
                )
        
        return feq(root1, root2)
        
        
"""
6 min: first draft
9 min: wrong answer
11 min: finished

Only issue was missing parentheses.  On proofreading, I found a bug and fixed it.
(The missing check for node1 is None or node2 is None)


Classic recursion algo

assume a function:

# returns true if node1 and node2 are flip-equivalent
feq(node1, node2)

def feq(node1, node2):

"""
