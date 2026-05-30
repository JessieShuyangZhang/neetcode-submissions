class TimeMap:
    def __init__(self):
        self.mp = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp or len(self.mp[key]) == 0:
            return ""

        tsvalues = self.mp[key]
        if tsvalues[-1][0] <= timestamp:
            return tsvalues[-1][1]
        if tsvalues[0][0] > timestamp:
            return ""
        l, r = 0, len(tsvalues) - 1
        ans = ""
        while l <= r:
            m = (l + r) // 2
            if tsvalues[m][0] > timestamp:
                r = m - 1
            elif tsvalues[m][0] < timestamp:
                ans = tsvalues[m][1]
                l = m + 1
            else:
                return tsvalues[m][1]
        return ans
