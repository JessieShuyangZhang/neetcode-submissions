class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visiting = set()
        completed = set()
        def hascycle(node, prev):
            if node in visiting:
                return True
            visiting.add(node)
            for nei in adj[node]:
                if nei==prev:
                    continue
                if hascycle(nei, node):
                    return True
            visiting.remove(node)
            completed.add(node)
            return False

        if hascycle(0, None) or (len(completed)<n):
            return False
        return True