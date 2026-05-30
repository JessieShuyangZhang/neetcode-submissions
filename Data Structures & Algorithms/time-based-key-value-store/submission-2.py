class TimeMap:
    def __init__(self):
        self.mp = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, arr = "", self.mp[key]
        l, r=0, len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m][0]<= timestamp:
                res = arr[m][1]
                l=m+1
            else:
                r=m-1
        return res
"""
[1,2,4,5] target:3, expected:2
l=0.r=3.m=1. 2<3. res=2. 
l=2.r.3 m=2, 4>3, 
r=1 break

[1,2,4,5] target:6, expected:5
l=0.r=3.m=1. 2<6. res=2. 
l=2.r=3.m=2. 4<6. res=4. 
l=3.r=3.m=3. 5<6. res=5. 
"""