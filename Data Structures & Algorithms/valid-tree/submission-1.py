class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        adj = defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()

        def dfs(x,last):
            if x in visited:
                return False
            
            visited.add(x)
            for nei in adj[x]:
                if nei == last:
                    continue
                if not dfs(nei,x):
                    return False
            return True

        if not dfs(0,None):
            return False
        if len(visited) < n:
            return False
        return True