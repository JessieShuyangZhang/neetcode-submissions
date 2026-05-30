# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pt = head
        for i in range(0,n):
            pt = pt.next
# [1,2,3,4,5] n = 5, pt->5
#^           ^
        prev = dummy
        while pt:
            prev = prev.next
            pt = pt.next

        prev.next = prev.next.next
        return dummy.next