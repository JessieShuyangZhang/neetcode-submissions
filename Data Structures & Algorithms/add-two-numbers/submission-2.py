# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1head = l1
        l2head = l2
        last = None
        while l1 and l2:
            s = l1.val + l2.val + carry
            if s>9:
                carry = 1
                l1.val = l2.val = s-10
            else:
                carry = 0
                l1.val = l2.val = s
            last = l2
            l1 = l1.next
            l2 = l2.next
        lr = l2
        res = l1head
        if l1:
            lr = l1
            res = l1head
        else: # either both empty or l2 nonempty
            lr = l2
            res = l2head
        while lr != None and carry > 0:
            s = lr.val + carry
            if s>9:
                carry = 1
                lr.val = s-10
            else:
                carry = 0
                lr.val = s
            last = lr
            lr = lr.next
        if carry == 1:
            last.next = ListNode(1)
        return res
