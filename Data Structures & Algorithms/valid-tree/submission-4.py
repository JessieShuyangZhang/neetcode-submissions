class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            res = x
            while par[res] != res:
                res = par[res]
            parent = res
            res = x
            while par[res] != parent:
                temp = par[res]
                par[res] = parent
                res = temp
            return parent

        def union(x,y):
            px,py = find(x), find(y)
            if px == py:
                return False
            if rank[px]>rank[py]:
                rank[px] += rank[py]
                par[py] = px
            else:
                rank[py] += rank[px]
                par[px] = py
            return True

        for x,y in edges:
            if not union(x,y):
                return False # cycle
        
        return max(rank) == n