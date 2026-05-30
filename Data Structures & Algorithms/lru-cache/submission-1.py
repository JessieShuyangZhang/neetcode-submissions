class DLLNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}  # key --> node
        self.head = DLLNode()  # point to node most recently used
        self.tail = DLLNode()  # point to node least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.mp) == self.capacity:
                # find the least recently used, delete
                lru = self.tail.prev
                self._remove(lru)
                del self.mp[lru.key]

            node = DLLNode(key, value)
            self.mp[key] = node
            self._add_to_front(node)

    