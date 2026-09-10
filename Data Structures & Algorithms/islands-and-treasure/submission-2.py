class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # INF = 2147483647 
        DIRS = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()        
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for d0, d1 in DIRS:
                    nr, nc = r+d0, c+d1
                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc]>0 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        
            dist += 1
                            
        return