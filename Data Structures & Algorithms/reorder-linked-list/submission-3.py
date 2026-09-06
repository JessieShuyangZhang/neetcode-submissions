# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return 
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        # last now points to the last node

        firsthalf = head
        for i in range(length//2):
            firsthalf = firsthalf.next
        # firsthalf now points at node 3 in [0, 1, 2, 3, 4, 5, 6]
# severe 3->4
        secondhalf = firsthalf.next 
        firsthalf.next = None

        # reverse secondhalf
        curr, prev = secondhalf, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        secondhalf = prev         #  6->5->4
        
        # merge
        firsthalf = head
        while secondhalf:
            first_next = firsthalf.next
            second_next = secondhalf.next

            firsthalf.next = secondhalf
            secondhalf.next = first_next

            firsthalf = first_next
            secondhalf = second_next
        