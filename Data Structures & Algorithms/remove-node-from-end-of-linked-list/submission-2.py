# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr: 
            N += 1
            curr = curr.next
        
        pos = N-n

        curr = head
        if pos == 0:
            head = head.next
            return head
        for i in range(1, pos):
            curr = curr.next
        curr.next = curr.next.next

        return head