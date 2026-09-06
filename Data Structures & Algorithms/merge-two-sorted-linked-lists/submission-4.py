# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedhead = ListNode()
        ptr = mergedhead
        while list1 and list2:
            if list1.val < list2.val:
                tmp = list1.next
                list1.next = None
                ptr.next = list1
                ptr = ptr.next
                list1 = tmp
            else:
                tmp = list2.next
                list2.next = None
                ptr.next = list2
                ptr = ptr.next
                list2 = tmp

        if list2 and list1 == None:
            ptr.next = list2
        elif list1 and list2 == None:
            ptr.next = list1
        return mergedhead.next