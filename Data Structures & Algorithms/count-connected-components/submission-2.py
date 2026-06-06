class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        size = [1] * n
        comp = n
        def find(x):
            while par[x]!=x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(x,y):
            px,py = find(x),find(y)
            if px == py:
                return 0
            if size[px] < size[py]:
                size[py] += size[px]
                par[px] = py
            else:
                size[px] += size[py]
                par[py] = px
            return 1
        
        for i,j in edges:
            comp -= union(i,j)
        return comp