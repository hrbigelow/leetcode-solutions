"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.
"""

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None: return l2
        elif l2 is None: return l1
        elif l1.val < l2.val:
            lo, hi = l1, l2
        else:
            lo, hi = l2, l1

        head = lo
        
        while lo is not None and hi is not None:
            if lo.next is None or hi.val <= lo.next.val:
                tmp = lo.next
                lo.next = hi
                lo, hi = hi, tmp
            else:
                lo = lo.next
        
        return head
