# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
# [0,1,2,3] slow: 1, fast: 3, cur: 2
# [3,2]
# [0,1,2,3,4] slow: 2  fast: None, cur: 3
# [4,3]
        cur = slow.next
        pre = slow.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        first, second = head, pre
        while second: 
            next1, next2 = first.next, second.next            
            first.next = second
            second.next = next1
            first = next1
            second = next2
        



        