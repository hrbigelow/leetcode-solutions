def report(node):
    print(f'node {node.val}')

def inorder_walk(node):
    if not node:            # TOP
        return
    inorder_walk(node.left) # LEFT
    report(node)            # REPORT
    inorder_walk(node.right) # RIGHT
                             # END

"""
        0
     1     2
   3   4 5   6

"""

TOP, LEFT, REPORT, RIGHT, END = range(5) 
def inorder_walk_explicit(node):
    ip = [TOP]
    st = [node]
    while st:
        node = st[-1]  # 0 1 3 - 
        site = ip[-1]  # LEFT LEFT RIGHT TOP
        if site == TOP:
            if not node:
                st.pop()
                ip.pop()
            else:
                ip[-1] = LEFT 
        elif site == LEFT:
            ip[-1] = REPORT
            ip.append(TOP)
            st.append(node.left)
        elif site == REPORT:
            report(node)
            ip[-1] = RIGHT
        elif site == RIGHT:
            ip[-1] = END
            st.append(node.right)
            ip.append(TOP)
        else:
            ip.pop()
            st.pop()


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

nodes = [Node(i) for i in range(7)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]

inorder_walk(nodes[0])
inorder_walk_explicit(nodes[0])



