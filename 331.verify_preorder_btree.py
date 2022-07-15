"""
One way to serialize a binary tree is to use preorder traversal. When we
encounter a non-null node, we record the node's value. If it is a null node, we
record using a sentinel value such as '#'.

For example, the above binary tree can be serialized to the string
"9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a
correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either
an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.
"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        toks = preorder.split(',')
        st = [-1] # simulates the 'main' program
        for t in toks:
            st.append(2 if t == '#' else 0)
            while st[-1] == 2:
                st.pop()
                if not st:
                    return False
                st[-1] += 1
            
            # print(st)
        
        return len(st) == 1 and st[0] == 0
        
        
"""
Took 50 minutes.  I had some trouble remembering that an explicit stack
should store a code 'address' and manage it accordingly.  Further, the stack should
start with an element representing the address in the main program.


"""
