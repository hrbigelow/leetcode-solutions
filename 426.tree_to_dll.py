"""
The recursive subproblem is to convert a BST into a doubly linked list, and
then return the head and tail of that list.  If we can do that, then
it is possible to join the result of the left and right and node, and return that

The subcases are that the left and right subtrees could be none.

This was tricky to properly treat the null cases on either side.  This is a similar thing
that happened with a different problem.

"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # join nodes a and b
        def join(a, b):
            if a and b:
                a.right = b
                b.left = a
            
        def linearize(node):
            if not node:
                return None, None
            left_head, left_tail = linearize(node.left)
            right_head, right_tail = linearize(node.right)

            join(left_tail, node)
            join(node, right_head)
            
            return left_head or node, right_tail or node

        head, tail = linearize(root)
        join(tail, head)
        
        return head
