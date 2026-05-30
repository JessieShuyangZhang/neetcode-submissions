# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, n = head, 1
        while cur and n < k:
            cur = cur.next
            n += 1
        if cur == None:
            return head
        
        remain = self.reverseKGroup(cur.next, k)

        cur = head
        pre = remain
        for _ in range(k):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre