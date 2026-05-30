class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict() # end: most recent; front: least recent
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value 
        if key in self.cache:
            self.cache.move_to_end(key)
        
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

