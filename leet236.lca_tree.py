class Solution:
    def lca(self, node, p, q):
        if node is None:
            return None, False, False
        left_lca, left_pdesc, left_qdesc = self.lca(node.left, p, q)
        if left_lca:
            return left_lca, True, True
        right_lca, right_pdesc, right_qdesc = self.lca(node.right, p, q)
        if right_lca:
            return right_lca, True, True
        pdesc = left_pdesc or right_pdesc or node == p
        qdesc = left_qdesc or right_qdesc or node == q
        lca_node = node if pdesc and qdesc else None

        return lca_node, pdesc, qdesc
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p, q)[0]


"""
The base case here returns the node if it's p, q, or None.  The fact that
it is returning a node at all is a signal that it 

The calling arguments are not interesting.  The only information we have is the
current node, as well as the constant, target nodes p and q.

The semantics of the returned node is that it is the lowest common ancestor of
either 0, 1, or 2 among the p and q, whichever is greatest.


This is an interesting use of the return value.  It doesn't maintain any
invariant, except the notion of the 


"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        elif left is None:
            return right
        elif right is None:
            return left
        else:
            return root

