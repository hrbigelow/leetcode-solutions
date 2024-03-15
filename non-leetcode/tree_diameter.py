"""
Q2. Given a Binary Tree, return the tree diameter, defined as the maximum number of
nodes traversed between any two nodes.  

This is recursively defined as the maximum between:

tree_diameter(node.left)
tree_dimenter(node.right)
depth(node.left) + 1 + depth(node.right)

so, we can return both tree_diameter and depth in one function
"""

def tree_diameter(root):
    def _rec(node):
        if node is None:
            return 0, 0 # tree_diam, (node depth)
        left_diam, left_depth = tree_diameter(node.left)
        right_diam, right_depth = tree_diameter(node.right)
        depth = 1 + max(left_depth, right_depth)
        diam = max(left_diam, right_diam, left_depth + right_depth + 1)
        return diam, depth

    diam, _ = _rec(root)
    return diam




