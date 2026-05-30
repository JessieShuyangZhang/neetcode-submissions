class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict() # end: most rec used; front:LRU

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            del self.od[key]
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)

