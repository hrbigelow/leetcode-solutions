"""

Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = None
        
        # search the tree rooted at node for the k'th (zero-indexed) in-order node,
        # return the index of the node for searching the remaining nodes, or
        # a negative number if it is already found
        def dfs(node, k):
            if not node or k < 0:
                return k
            
            # print(node.val, k)
            
            k = dfs(node.left, k)
            k -= 1 # decrement k, since we have now visited another node
            if k == 0:
                self.val = node.val
                return 0

            k = dfs(node.right, k)
            return k
            
        dfs(root, k)
        return self.val

"""
The key to understanding this was to realize the distinction between a dfs call and a node being logically 'visited'.
The two are not the same.  In DFS in-order traversal, the first call is to the root of the tree, but the first node that is 
visited is the extreme left leaf.  The pattern is:

def dfs(node):
    if not node:
        return
    dfs(node.left)
    visit(node)  # <= apply 'visit' logic here
    dfs(node.right)
    
And the visit logic should apply there.  In this case, it is to decrement k, which is the number
of nodes needing to be visited.

"""
