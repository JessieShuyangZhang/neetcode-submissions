    
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {} # key: Node
        self.llhead = ListNode(0,0)
        self.lltail = ListNode(0,0)
        self.llhead.next = self.lltail
        self.lltail.prev = self.llhead

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.remove(node)
            self.insertFront(node)
            return node.val
        return -1

    def remove(self, node: ListNode) -> None:
        prev_n = node.prev
        next_n = node.next
        prev_n.next = next_n
        next_n.prev = prev_n
        
    def insertFront(self, node: ListNode) -> None: 
        node.next = self.llhead.next
        node.prev = self.llhead
        self.llhead.next = node
        node.next.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])        
        self.mp[key] = ListNode(key,value)
        self.insertFront(self.mp[key])
        if len(self.mp) > self.capacity:
            lru_n = self.lltail.prev
            self.remove(lru_n)
            self.mp.pop(lru_n.key)
