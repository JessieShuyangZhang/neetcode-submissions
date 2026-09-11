class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [1, 0]] # [-1, 0], [0, -1],
        dsu = DSU(ROWS * COLS)
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0":
                    continue
                islands += 1
                for d0, d1 in DIRS:
                    a, b = i+d0, j+d1
                    if (a in range(ROWS) and b in range(COLS) and grid[a][b] == "1"):
                        islands -= dsu.union(i * COLS + j, a * COLS + b)
        return islands

class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, a) -> int:
        while self.par[a] != a:
            a = self.par[self.par[a]]
        return a

    def union(self, a, b) -> int:
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a == par_b:
            return 0
        if self.rank[par_a] > self.rank[par_b]:
            self.rank[par_a] += self.rank[par_b]
            self.par[par_b] = par_a
        else:
            self.rank[par_b] += self.rank[par_a]
            self.par[par_a] = par_b
        return 1
