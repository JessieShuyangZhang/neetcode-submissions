class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        
        minh = [] # (edgeweight, node)
        totalcost = 0
        heapq.heappush(minh, (0, points[0]))
        visited = set()
        while minh:
            cost, node = heapq.heappop(minh)
            if tuple(node) in visited:
                continue
            visited.add(tuple(node))
            totalcost += cost
            for p in points:
                if tuple(p) in visited:
                    continue
                heapq.heappush(minh, (distance(p, node), p))
        return totalcost