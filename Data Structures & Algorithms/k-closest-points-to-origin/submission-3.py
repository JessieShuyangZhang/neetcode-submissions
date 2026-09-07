class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minhp = [] # (-euc_dist, points_index)
        for i in range(len(points)):
            x, y=points[i][0],points[i][1]
            euc = (x**2+y**2)**0.5
            heapq.heappush(minhp, (-euc,i))
            while len(minhp) > k:
                heapq.heappop(minhp)
        return [points[i] for _, i in minhp]