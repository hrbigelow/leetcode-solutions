"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        source = head
        node_map = {}
        dummy = ListNode()
        target = dummy
        
        while source is not None:
            target.next = Node(source.val)
            target = target.next
            node_map[source] = target
            source = source.next
            
        source = head
        target = dummy.next
        
        while target is not None:
            if source.random in node_map:
                target.random = node_map[source.random]
            source = source.next
            target = target.next
            
        return dummy.next
        
        
        
"""
12 min: first draft
15 min: finished (no issues)

In the first pass, node_map gets an entry for each source.  it points to
the clone

In the second pass, source and target always point to the matching clones,
and the node map is used whenever it applies

"""
