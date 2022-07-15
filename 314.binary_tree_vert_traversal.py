"""
Given the root of a binary tree, return the vertical order traversal of its
nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

"""

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dd = defaultdict(lambda: [])

        dq = [(root, 0)]
        while dq:
            node, col = dq.pop(0)
            if node is None:
                continue
            dd[col].append(node.val)
            dq.append((node.left, col-1))
            dq.append((node.right, col+1))
            
        return [dd[k] for k in sorted(dd.keys())]
        
    
"""
Solved in 26 minutes.  First attempt used dfs, which doesn't visit nodes in depth order.
"""
