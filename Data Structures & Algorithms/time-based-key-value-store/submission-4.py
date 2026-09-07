class TimeMap:

    def __init__(self):
        self.mp = {} # key -> (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp: 
            self.mp[key] = []
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp or self.mp[key][0][0] > timestamp: 
            return ""
        arr = self.mp[key]
        l, r=0, len(arr)-1
        res = ""
        while l<=r:
            m=(l+r)//2
            if arr[m][0] > timestamp:
                r = m-1
            else:
                res = arr[m][1]
                l = m+1
        return res