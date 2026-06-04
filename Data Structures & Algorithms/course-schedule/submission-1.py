class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited=set()
        for a,b in prerequisites:
            adj[a].append(b)

        def dfs(x,visited):
            if x in visited:
                return False
            if x not in adj:
                return True
            visited.add(x)
            for y in adj[x]:
                if not dfs(y,visited):
                    return False
            visited.remove(x)
            adj[x] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True