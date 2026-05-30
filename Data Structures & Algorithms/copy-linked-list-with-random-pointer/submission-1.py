"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {} # original -> copy
        mp[None] = None
        cur = head
        res = dummy = Node(0)
        prev= None
        while cur:
            copy = Node(cur.val)
            if prev: 
                prev.next = copy
            else:
                dummy.next = copy
            mp[cur] = copy
            prev = copy
            cur = cur.next
        cur = dummy.next
        for ori, copy in mp.items():
            if copy != None:
                copy.random = mp[ori.random] if ori!=None else None
        return dummy.next