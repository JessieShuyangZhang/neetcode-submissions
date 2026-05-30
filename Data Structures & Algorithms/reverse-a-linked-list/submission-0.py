# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        res = ListNode(head.val, None)
        
        while head.next :
            newnode = ListNode(head.next.val, res)
            res = newnode
            head = head.next

        return res