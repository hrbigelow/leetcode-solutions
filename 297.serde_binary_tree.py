"""
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a
binary tree. You do not necessarily need to follow this format, so please be
creative and come up with different approaches yourself.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ser = ''
        if root is None: return ser
        
        def dfs(node):
            nonlocal ser
            
            ser += str(node.val)
            if node.left is not None:
                ser += 'L'
                dfs(node.left)
            
            if node.right is not None:
                ser += 'R'
                dfs(node.right)
            
            ser += '$' # signifies the end of children
            
        dfs(root)
        # print(ser)
        return ser
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        
        st = []
        root = TreeNode(0)
        cur = root
        is_neg = False
        
        for c in data[:-1]:
            if c == '$': # got a Null value
                cur = st.pop()

            elif c == 'L':
                cur.left = TreeNode(0)
                st.append(cur)
                cur = cur.left

            elif c == 'R':
                cur.right = TreeNode(0)
                st.append(cur)
                cur = cur.right
            
            elif c.isdigit():
                p = int(c) if cur.val >= 0 else -int(c)
                cur.val = cur.val * 10 + p
                if is_neg:
                    cur.val = - cur.val
                    is_neg = False
                
            elif c == '-':
                is_neg = True
            
        return root        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""
Took about 1.5 hours.  Was distracted.



"""
