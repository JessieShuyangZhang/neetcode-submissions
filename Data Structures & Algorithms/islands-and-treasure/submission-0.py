class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        def bfs(r,c):
            q = deque()
            q.append([r,c])
            visited = set()
            while q:
                x,y = q.popleft()
                for d0,d1 in dirs:
                    nx,ny = x+d0,y+d1
                    if (-1<nx<ROWS and -1<ny<COLS 
                        and grid[nx][ny]>0 
                        and (nx,ny) not in visited):
                        grid[nx][ny] = min(grid[nx][ny],grid[x][y]+1)
                        q.append([nx,ny])
                        visited.add((nx,ny))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i,j)

