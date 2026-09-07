class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negstones = [-x for x in stones]
        heapq.heapify(negstones)
        while len(negstones)>=2:
            one = -heapq.heappop(negstones)
            two = -heapq.heappop(negstones)
            if one == two: 
                continue
            heapq.heappush(negstones, -abs(one - two))
        if len(negstones) == 1:
            return -negstones[0]
        return 0