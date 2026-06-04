class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[a].append(b)

        res = []
        visited, cycle =set(), set()
        
        def dfs(x):
            if x in cycle: 
                return False
            # if x not in adj or len(adj[x]) == 0:
            if x in visited:
                return True
            
            cycle.add(x)
            for pre in adj[x]:
                if not dfs(pre):
                    return False
                # if pre not in taken: # is this right???
                #     res.append(pre) 
                #     taken.add(pre)
            cycle.remove(x)
            visited.add(x)
            res.append(x)
            return True

        for n in range(numCourses):
            if n not in visited:
                if not dfs(n):
                    return []
        return res