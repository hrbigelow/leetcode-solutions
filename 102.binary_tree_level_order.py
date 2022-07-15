"""
Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).
"""
"""
Solved both in about 20 minutes, starting with the iterative solution.  At first I thought it
might be possible to do the iterative solution without pushing the auxiliary depth information
but I didn't figure out how to avoid that.

How to do this recursively?  You really can't do BFS recursively.  But you could do
a DFS while keeping track of depth

"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        
        # add all of the nodes in the node subtree, where
        # node is at depth
        def add_rec(node, depth):
            if not node:
                return
            if len(results) <= depth:
                results.append([])
            results[depth].append(node.val)
            add_rec(node.left, depth+1)
            add_rec(node.right, depth+1)
        
        add_rec(root, 0)
        return results
    


"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        d = deque([(root, 0)])
        results = []
        while d:
            node, level = d.popleft()
            if not node:
                continue
            if len(results) < level + 1:
                   results.append([])
            results[level].append(node.val)
            d.extend([(node.left, level+1), (node.right, level+1)])
        
        return results
""" 
