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
