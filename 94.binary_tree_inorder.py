class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = [root]
        results = []  # rule: if integer, push to results, otherwise, recurse
        
        while st:
            node_or_int = st.pop()
            if isinstance(node_or_int, int):
                results.append(node_or_int)
                continue
            
            node = node_or_int
            if not node:
                continue
            st.extend([node.right, node.val, node.left])
            
        return results
    
"""
Solved the iterative solution in about 20 minutes.  I had the idea to use a hybrid
stack that represents different types of information.  In this case, the recursive function body included
three things - the two recursive calls and the pushing of the node value.

The tricky thing to realize is that the items in the stack are *processed* in reverse order of being added.
Therefore, we need to add them in reverse order of where they appear in the function body.

"""            


"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            results.append(node.val)
            traverse(node.right)
            
        traverse(root)
        return results
""" 

