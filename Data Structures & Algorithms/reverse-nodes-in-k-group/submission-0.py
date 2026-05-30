# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def enoughRemains(self, head: Optional[ListNode], k: int) -> bool:
    #     i = 0
    #     cur = head
    #     while cur and i < k: 
    #         i += 1
    #         cur = cur.next
    #     return i >= k

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base case
        i = 0
        cur = head
        if not cur: 
            return None
        while cur and i < k: 
            i += 1
            cur = cur.next
        if i < k:
            return head # do not reverse if not enough left
        # there's enough left, skip first k then recur to next k's
        remainhead = self.reverseKGroup(cur, k)
        last = head
        newhead = self.reverseKNodes(head,k)
        last.next = remainhead
        return newhead

    def reverseKNodes(self,head: Optional[ListNode], k: int)-> Optional[ListNode]:
        cur = head
        prev = None
        i = 0
        while cur and i < k: 
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            i += 1
        return prev
