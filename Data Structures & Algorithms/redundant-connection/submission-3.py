class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for i in range(n+1)]
        degrees = [0] * (n+1)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            degrees[i] += 1
            degrees[j] += 1
        q = deque()
        for node, degree in enumerate(degrees):
            if degree == 1:
                q.append(node)
        visit = set()
        while q:
            node = q.popleft()
            visit.add(node)
            for nei in adj[node]:
                degrees[nei] -= 1
                if degrees[nei] == 1:
                    q.append(nei)
        for i in range(n-1, -1, -1):
            a, b = edges[i]
            if a not in visit and b not in visit:
                return [a, b]