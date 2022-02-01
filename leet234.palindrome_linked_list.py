"""

"""
# 64 ms
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        pre, cur, nxt = None, head, head.next
        sentinel = cur
        
        while sentinel:
            
            if sentinel.next is None:
                # list length is odd.
                rhead = ListNode(cur.val)
                rhead.next = nxt
                break

            elif sentinel.next.next is None:
                # list length is even
                rhead = nxt
                break
            else:
                sentinel = sentinel.next.next
                cur.next = pre
                pre, cur, nxt = cur, nxt, nxt.next

        lhead = cur
        lhead.next = pre

        while lhead and rhead:
            if lhead.val != rhead.val:
                return False
            lhead = lhead.next
            rhead = rhead.next
        return True


# 48 ms
# However, this uses O(n) memory
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

