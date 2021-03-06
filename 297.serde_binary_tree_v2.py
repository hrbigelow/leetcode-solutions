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
        def ser_rec(node):
            if node is None:
                return ''
            lstr = ser_rec(node.left)
            rstr = ser_rec(node.right)
            return f'{node.val}({lstr},{rstr})'
        
        return ser_rec(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deser_rec(i):
            if i == len(data) or data[i] in ',)':
                return None, i
            
            val = 0
            neg = False
            while data[i].isdigit() or data[i] == '-':
                if data[i] == '-':
                    neg = True
                else:
                    val *= 10
                    val += int(data[i])
                i += 1
            if neg:
                val = -val
            
            node = TreeNode(val)
            node.left, i = deser_rec(i+1)
            node.right, i = deser_rec(i+1)
            return node, i+1
            
        root, _ = deser_rec(0)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
What would be a template?

T: V(T,T) # value and two sub-trees
T: ''  # empty tree




"""
