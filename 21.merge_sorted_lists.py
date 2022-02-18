# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
base case:  one or both heads are None => return the non-null head if any
recurrence:  take the lesser of the two heads the main head.  then
             merge the resulting lists
             
why this works.  

"""
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: return l2
        elif l2 is None: return l1
        else:
            if l1.val < l2.val:
                h, l1 = l1, l1.next
            else:
                h, l2 = l2, l2.next
                
            h.next = self.mergeTwoLists(l1, l2)
            return h
        
