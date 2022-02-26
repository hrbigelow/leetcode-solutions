# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import heapq
    
    class NodeIndex():
        
        @classmethod
        def set_lists(cls, lists):
            cls.lists = lists
            
        def __init__(self, i):
            self.ind = i
        
        def __lt__(self, other):
            self_val = float('inf') if self.lists[self.ind] is None else self.lists[self.ind].val
            other_val = float('inf') if self.lists[other.ind] is None else self.lists[other.ind].val
            return self_val < other_val
        
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        
        head = ListNode()
        merged_tail = head

        self.NodeIndex.set_lists(lists)
        hq = [self.NodeIndex(i) for i in range(k)]
        heapq.heapify(hq)
        
        while True:
            min_head = heapq.heappop(hq)
            if lists[min_head.ind] is None:
                break
            
            merged_tail.next = lists[min_head.ind]
            lists[min_head.ind] = lists[min_head.ind].next
            merged_tail = merged_tail.next
            
            # min_head now refers to the next node, so may settle somewhere else
            # in the heap
            heapq.heappush(hq, min_head)
        
        return head.next
        
        
"""
8 min first draft
9 min test (time limit exceeded - realized I need the heapq)
28 min finished (3 or more struggles with how to define the wrapper class)

Checks:
"""
