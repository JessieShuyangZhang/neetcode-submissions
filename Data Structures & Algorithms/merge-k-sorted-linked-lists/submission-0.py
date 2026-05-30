# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self,other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode(0)
        cur = res
        heap = []
        for l in lists:
            if l != None: 
                heapq.heappush(heap, NodeWrapper(l))

        while len(heap) > 0:
            smallest = heapq.heappop(heap).node
            cur.next = smallest
            cur = cur.next
            if smallest.next:
                heapq.heappush(heap, NodeWrapper(smallest.next))
        return res.next