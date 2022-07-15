"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child
pointer points to the next node in the list and the left child pointer is
always null.  The "linked list" should be in the same order as a pre-order
traversal of the
binary tree.

"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def rec(node):
            if node is None: return node
            
            if not node.left and not node.right:
                return node
            
            left_tail = rec(node.left)
            right_tail = rec(node.right)
            
            if left_tail is not None:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            return right_tail or left_tail
        
        rec(root)
        
        
"""
Solved in 20 minutes.  Took about 10 attempts.  The recursive relation itself
was easy to see, but dealing with the three non-base cases of:

node.left and node.right
not node.left and node.right
node.left and not node.right

At first I didn't consider these different cases and just assumed everything was
like the first case.

Secondly, I forgot to set node.left to None

"""
