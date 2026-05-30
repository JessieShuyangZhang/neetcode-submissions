# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nodeb4group = dummy
        newHead = None

        while nodeb4group:
            kth = self.getKth(nodeb4group.next,k)
            if not kth:
                break
            i = k
            groupStart = nodeb4group.next
            cur, prev = groupStart, kth.next
            while i > 0:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                i -= 1
            nodeb4group.next = prev
            nodeb4group = groupStart
        return dummy.next


    def getKth(self,head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, i = head, k
        while cur and i > 1:
            cur = cur.next
            i -= 1
        return cur
