class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minh, res = [], [] # dist, i
        for i, point in enumerate(points):
            x,y = point[0],point[1]
            dist = (x**2 + y**2)**0.5
            minh.append((dist,i))
        heapq.heapify(minh)
        while k > 0:
            d, i = heapq.heappop(minh)
            res.append(points[i])
            k-=1
        return res
