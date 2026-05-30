# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None # in each iteration this will become next node

        while curr:
            temp = curr.next # keep track of original next node
            curr.next = prev
            prev = curr 
            curr = temp
        return prev