"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

"""
:ene
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        stack = []
        psuedoHead = Node(0, None, head, None)
        prev = psuedoHead
        stack.append(head)
        while stack:
            current = stack.pop()
            prev.next = current
            current.prev = prev
            if current.next:
                stack.append(current.next)
            if current.child:
                stack.append(current.child)
                current.child = None
            prev = current
        psuedoHead.next.prev = None
        return psuedoHead.next


"""



"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flat_ext(cur):
            tail = cur
            sub_tail = cur
            while cur:
                nxt = cur.next
                if cur.child is not None:               
                    sub_head = cur.child
                    sub_tail = flat_ext(sub_head)
                    cur.child = None     # 2
                    cur.next = sub_head  # 1
                    sub_head.prev = cur  # 5
                    sub_tail.next = nxt  # 3
                    if nxt is not None:
                        nxt.prev = sub_tail  # 4
                    tail = sub_tail
                else:
                    tail = cur
                cur = nxt
            
            return tail

        flat_ext(head)
        return head

