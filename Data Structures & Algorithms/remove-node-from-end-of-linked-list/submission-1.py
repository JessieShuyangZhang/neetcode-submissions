# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseLL(head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        #1. reverse the linked list
        reverse = reverseLL(head)

        #2. use counter and remove the nth node starting from prev
        i = 1
        last = reverse
        if n == 1:
            return reverseLL(last.next)
        while i < n-1:
            last = last.next
            i += 1
        if n > 1 or last.next != None:
            last.next = last.next.next
        else:  # n == 1 and last.next==None
            return None;
        # reverse prev back
        return reverseLL(reverse)