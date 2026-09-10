class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adj = [[] for i in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visiting = set()
        def hascycle(node, prev):
            if node in visiting:
                return True
            visiting.add(node)
            for nei in adj[node]:
                if nei==prev:
                    continue
                if hascycle(nei, node):
                    return True
            return False

        if hascycle(0, None) or (len(visiting)<n):
            return False
        return True