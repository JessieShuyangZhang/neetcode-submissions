class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS=[[0,1],[0,-1],[1,0],[-1,0]]
        maxarea = 0

        def bfs(r,c):
            nonlocal maxarea
            q = deque()
            q.append((r,c))
            grid[r][c]=0
            area = 1
            while q: 
                c0,c1 = q.popleft()
                for d0, d1 in DIRS:
                    nr, nc = c0+d0, c1+d1
                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc]==1):
                        area += 1
                        grid[nr][nc] = 0
                        q.append((nr,nc))
            maxarea = max(maxarea, area)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    bfs(i,j)
        return maxarea