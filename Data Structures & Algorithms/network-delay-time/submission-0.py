class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        totaltime = 0
        adjmp = defaultdict(list)

        for u, v, t in times:
            unei = adjmp.get(u, [])
            unei.append((v,t))
            adjmp[u] = unei
        
        minh = [(0, k)] # pathtime, node
        heapq.heapify(minh)
        while minh:
            pathtonode, node = heapq.heappop(minh)
            if node in visited:
                continue
            visited.add(node)
            totaltime = max(totaltime, pathtonode)
            for n1, t1 in adjmp[node]:
                if n1 in visited:
                    continue
                heapq.heappush(minh, (pathtonode+t1, n1))

        if len(visited) != n:
            return -1
        return totaltime
