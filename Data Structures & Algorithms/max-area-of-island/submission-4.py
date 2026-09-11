class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [1, 0]]
        dsu = DSU(ROWS * COLS)
        hasland = False
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    continue
                hasland = True
                for x, y in DIRS:
                    a, b = i + x, j + y
                    if a in range(ROWS) and b in range(COLS) and grid[a][b] == 1:
                        dsu.union(i * COLS + j, a * COLS + b)
        if hasland:
            return max(dsu.rank)
        else:
            return 0


class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, a):
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]

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
