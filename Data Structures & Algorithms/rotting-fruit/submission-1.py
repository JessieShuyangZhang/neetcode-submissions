class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        rottime = {} # (i,j)-> time it rots

        def bfs(r,c):
            q = deque()
            q.append([r,c,0])
            visited = set()
            while q:
                x,y,t = q.popleft()
                for d0,d1 in dirs:
                    nx,ny=x+d0,y+d1
                    if (-1<nx<ROWS and -1<ny<COLS
                        and grid[nx][ny] == 1
                        and (nx,ny) not in visited):
                        rott = min(t+1,rottime.get((nx,ny),float('inf')))
                        rottime[(nx,ny)] = rott                        
                        q.append([nx,ny,rott])
                        visited.add((nx,ny))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    bfs(i,j)
        totalrottime=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    if (i,j) not in rottime:
                        return -1
                    totalrottime = max(totalrottime,rottime[(i,j)])
        return totalrottime