class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited,cycle = set(),set()

        def dfs(x,last):
            if x in cycle:
                return False
            
            cycle.add(x)
            for nei in adj[x]:
                if nei == last:
                    continue
                if not dfs(nei,x):
                    return False
            cycle.remove(x)
            visited.add(x)
            return True

        if not dfs(0,None):
            return False
        if len(visited) < n:
            return False
        return True