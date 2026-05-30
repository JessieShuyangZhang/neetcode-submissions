# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle (slow's stopping point)
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow
        slow = slow.next
        mid.next = None

        # 2. reverse 2nd half
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev
        # 3. now prev is the reversed half; merge 2 linked lists
        while second: 
            tmp1 = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp1
            first = tmp1
            second = tmp2

        
