# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        def dfs(node, depth): # node is the current node being visited.  depth is its depth
            if node is None: return
            if depth == len(view):
                view.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root, 0)
        return view
    
        
"""
Finished in 10 minutes.

My first attempt was logically wrong.  I had tried a greedy approach, but it
turns out this requires a potentially full traversal.  This is because the
visible node can at the next depth can be on any subtree.

Other solutions use a BFS implementation with explicit deque.  This
will be more memory intensive but probably faster.

"""
