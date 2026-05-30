# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head
        for i in range(n):
            r = r.next
        if not r: # need to remove first node
            return head.next; 

        while r.next:
            l = l.next
            r = r.next

        l.next = l.next.next
        return head