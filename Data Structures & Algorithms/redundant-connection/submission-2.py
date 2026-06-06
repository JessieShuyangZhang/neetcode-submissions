class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        size = [1]*(len(edges)+1)
        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(x,y):
            px,py = find(x),find(y)
            if px == py:
                return True
            if size[px] < size[py]:
                size[py] += size[px]
                par[px] = py
            else:
                size[px] += size[py]
                par[py] = px
            return False
        for x, y in edges:
            if union(x,y):
                return [x,y]
            