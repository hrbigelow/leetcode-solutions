class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)



def max_heights(root):
    heights = {}
    
    def dfs(node):
        if node is None:
            return 0
    
        left_height = dfs(node.left)
        right_height = dfs(node.right)

        height = max(left_height, right_height) + 1
        heights[node.val] = height
        return height
    
    _ = dfs(root)
    return heights




# explicit stack version
class StackState:
    def __init__(self, node, call_addr):
        self.node = node
        self.call_addr = call_addr
        self.at = 0
        self.left_height = None
        self.right_height = None
        self.ret = None


# 

def make_tree(vals):
    nodes = [None if val is None else TreeNode(val) for val in vals]

    i, j = 0, 1
    while j != len(nodes):
        parent = nodes[i]
        if parent is not None:
            parent.left = nodes[j]
            parent.right = nodes[j+1]
            j += 2
        i += 1

    return nodes[0]



def max_heights_stack(root):
    heights = {}

    def dfs_stack(node):
        st = [StackState(node, -1)]
        while st:
            call = st[-1]
            if call.at == 0:
                if call.node is None:
                    call.left_height = -1
                    call.right_height = -1
                    call.at = 2

                else:
                    st.append(StackState(call.node.left, call.at))
                    call.at = 1

            elif call.at == 1:
                st.append(StackState(call.node.right, call.at))
                call.at = 2

            elif call.at == 2:
                call.ret = max(call.left_height, call.right_height) + 1
                if call.node is not None:
                    heights[call.node.val] = call.ret
                st.pop()

                if call.call_addr == -1:
                    return call.ret
                elif call.call_addr == 0:
                    st[-1].left_height = call.ret
                elif call.call_addr == 1:
                    st[-1].right_height = call.ret

    _ = dfs_stack(root)
    return heights

