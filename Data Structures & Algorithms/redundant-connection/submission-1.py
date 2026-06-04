class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        cycle = set()
        cyclenodes = set()
        cyclestart = -1
        def dfs(x,parent):
            nonlocal cyclestart
            if x in cycle:
                cyclestart = x
                cyclenodes.add(x)
                return True

            cycle.add(x)
            for nei in adj[x]:
                if nei == parent:
                    continue
                if dfs(nei,x):
                    if nei != cyclestart:
                        cyclenodes.add(nei)
                    return True
            # cycle.remove(x)
            return False

        dfs(1,None)
        for i in reversed(edges):
            if i[0] in cyclenodes and i[1] in cyclenodes:
                return i