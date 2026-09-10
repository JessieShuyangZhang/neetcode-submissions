class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0,-1],[0,1],[1,0],[-1,0]]
        visited = set()
        res = 0

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                c0, c1 = q.popleft()
                for d0, d1 in DIRS:
                    nx, ny = c0+d0, c1+d1
                    if (nx in range(ROWS) and ny in range(COLS) and grid[nx][ny]=="1" and (nx,ny) not in visited):
                        q.append((nx,ny))
                        visited.add((nx,ny))
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    bfs(i, j)
        return res

