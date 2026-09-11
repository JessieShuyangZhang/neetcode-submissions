class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, a):
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]
    def union(self,a,b):
        apar = self.find(a)
        bpar = self.find(b)
        if apar == bpar: 
            return 0
        if self.rank[apar] > self.rank[bpar]:
            self.rank[apar] += self.rank[bpar]
            self.par[bpar] = apar
        else:
            self.rank[bpar] += self.rank[apar]
            self.par[apar] = bpar
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        count = n
        for a, b in edges:
            count -= dsu.union(a,b)
        return count