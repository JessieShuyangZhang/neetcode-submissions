class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        components = 0
        def dfs(x,parent):
            if x in visited:
                return             
            visited.add(x)
            for nei in adj[x]:
                if nei == parent:
                    continue
                dfs(nei,x)            
        
        for i in range(n):
            if i not in visited:
                dfs(i,None)
                components += 1
        return components