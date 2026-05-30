# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1cur = l1
        l2cur = l2
        l1last = l1
        l2last = l2
        while l1cur and l2cur:
            s = l1cur.val + l2cur.val + carry
            if s > 9:
                carry = 1
                l1cur.val = l2cur.val = s - 10
            else:
                carry = 0
                l1cur.val = l2cur.val = s
            l1last = l1cur
            l1cur = l1cur.next
            l2last = l2cur
            l2cur = l2cur.next
        
        # check which list still has remains, if its l1 then reroute l2last to point to l1cur
        if l1cur:
            l2last.next = l1cur
            l2cur = l2last.next

        while l2cur:
            s = l2cur.val + carry
            if s>9:
                carry = 1
                l2cur.val = s-10
            else:
                l2cur.val = s
                return l2
            l2last = l2cur
            l2cur = l2cur.next
        if carry == 1:
            l2last.next = ListNode(1, None)
            
        return l2
