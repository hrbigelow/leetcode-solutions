class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = None
        
        def dfs(node, k):
            if not node:
                return k
            
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
