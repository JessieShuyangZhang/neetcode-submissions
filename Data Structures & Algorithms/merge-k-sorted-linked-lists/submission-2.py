# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = 0
        r = len(lists)-1
        m = (l+r)//2
        if l>r:
            return None
        elif l==r:
            return lists[0]
        l1 = self.mergeKLists(lists[l:m+1])
        l2 = self.mergeKLists(lists[m+1:r+1])
        dummy = ListNode(0)
        prev = dummy
        while l1 and l2:
            if l1.val < l2.val: 
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next 
            prev = prev.next

        prev.next = l1 or l2
        return dummy.next
