# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        if n <=2:
            return;
        else: 
            self.recur(n, head)
        
    def recur(self, length, head: Optional[ListNode]) -> None:
        if length <= 0:
            return
        if length <= 2:
            return head
    
        last = head
        prev = None
        for i in range(length-1):
            prev = last
            last = last.next
    
        prev.next = None  # sever the link to last
        self.recur(length-2, head.next)
        last.next = head.next
        head.next = last