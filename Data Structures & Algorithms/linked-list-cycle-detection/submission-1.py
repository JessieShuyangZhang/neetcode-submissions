# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head != None: 
            if head not in seen:
                seen.add(head)
            else:
                return True
            head = head.next
        
        return False